
import os
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
import app as app_module


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as test_client:
        with test_client.session_transaction() as session:
            session["user_id"] = 1
            session["role"] = "Student"
            session["full_name"] = "Test Student"

        yield test_client


def test_empty_chatbot_message(client):
    response = client.post(
        "/api/chatbot",
        json={"message": ""}
    )

    assert response.status_code == 400
    assert response.get_json()["success"] is False


def test_long_chatbot_message(client):
    response = client.post(
        "/api/chatbot",
        json={"message": "a" * 2001}
    )

    assert response.status_code == 400
    assert response.get_json()["success"] is False


def test_chatbot_success(client, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    monkeypatch.setattr(
        app_module,
        "chatbot_answer",
        lambda message: "Verified campus notice"
    )

    fake_client = Mock()
    fake_client.models.generate_content.return_value = (
        SimpleNamespace(text="Here is your campus answer.")
    )

    monkeypatch.setattr(
        app_module.genai,
        "Client",
        lambda api_key: fake_client
    )

    response = client.post(
        "/api/chatbot",
        json={"message": "Show me campus notices"}
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["success"] is True
    assert "campus answer" in data["reply"]


def test_gemini_quota_fallback(client, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    monkeypatch.setattr(
        app_module,
        "chatbot_answer",
        lambda message: "Verified campus notice"
    )

    quota_error = Exception("Quota exhausted")
    quota_error.code = 429

    fake_client = Mock()
    fake_client.models.generate_content.side_effect = quota_error

    monkeypatch.setattr(
        app_module.genai,
        "Client",
        lambda api_key: fake_client
    )

    response = client.post(
        "/api/chatbot",
        json={"message": "Show me campus notices"}
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["success"] is True
    assert "Verified campus notice" in data["reply"]

##


def test_chatbot_requires_login():
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:
        response = client.post(
            "/api/chatbot",
            json={"message": "Show me campus notices"},
            follow_redirects=False
        )

        # An unauthenticated user must not receive a successful API response.
        assert response.status_code in (302, 401, 403)

##
def test_student_cannot_access_admin_dashboard():
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:
        # Simulate a logged-in student.
        with client.session_transaction() as session:
            session["user_id"] = 1
            session["role"] = "Student"
            session["full_name"] = "Test Student"

        response = client.get(
            "/admin/dashboard",
            follow_redirects=False
        )

        # A student must not receive the admin dashboard successfully.
        assert response.status_code in (302, 401, 403)

##

@pytest.mark.parametrize(
    "url",
    [
        "/admin/students",
        "/admin/faculty",
        "/admin/notices",
        "/admin/timetable",
        "/admin/events",
    ],
)
def test_student_cannot_access_admin_management_pages(url):
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:
        with client.session_transaction() as session:
            session["user_id"] = 1
            session["role"] = "Student"
            session["user_name"] = "Test Student"

        response = client.get(url, follow_redirects=False)

        assert response.status_code in (302, 401, 403), (
            f"Student was not blocked from {url}. "
            f"Received HTTP {response.status_code}"
        )

##

@pytest.mark.parametrize(
    "url",
    [
        "/student",
        "/student/dashboard",
    ],
)
def test_admin_cannot_access_student_pages(url):
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:
        with client.session_transaction() as session:
            session["user_id"] = 1
            session["role"] = "Admin"
            session["user_name"] = "Test Admin"

        response = client.get(url, follow_redirects=False)

        assert response.status_code in (302, 401, 403), (
            f"Admin was not blocked from {url}. "
            f"Received HTTP {response.status_code}"
        )

##

@pytest.mark.parametrize(
    "url",
    [
        "/admin/dashboard",
        "/admin/students",
        "/admin/faculty",
        "/admin/notices",
        "/admin/timetable",
        "/admin/events",
        "/student/dashboard",
        "/chatbot",
    ],
)
def test_protected_pages_require_login(url):
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:
        response = client.get(url, follow_redirects=False)

        assert response.status_code in (302, 401, 403), (
            f"Unauthenticated user accessed {url}. "
            f"Received HTTP {response.status_code}"
        )

##
def test_inactive_user_cannot_login(monkeypatch):
    app_module.app.config["TESTING"] = True

    fake_user = {
        "user_id": 10,
        "full_name": "Inactive Test User",
        "email": "inactive@example.com",
        "password_hash": "dummy-password-hash",
        "role": "Student",
        "is_active": 0,
    }

    monkeypatch.setattr(
        app_module,
        "fetch_one",
        lambda query, params=(): fake_user
        if "FROM users" in query
        else None,
    )

    with app_module.app.test_client() as client:
        response = client.post(
            "/login",
            data={
                "email": "inactive@example.com",
                "password": "TestPassword123!",
            },
            follow_redirects=False,
        )

        with client.session_transaction() as session:
            assert "user_id" not in session

        assert response.status_code in (200, 302, 401, 403)


