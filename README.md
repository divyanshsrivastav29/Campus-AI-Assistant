# Campus AI Assistant

An AI-powered campus information and management system built using Python, Flask, MySQL, HTML, CSS, JavaScript, and Google Gemini AI.

## 1. Project Overview

Campus AI Assistant is a web-based application designed to make campus information easily accessible to students and administrators.

The system provides role-based login, campus information management, timetable access, notices, events, and an AI-powered chatbot to answer campus-related questions.

## 2. Objectives

- Provide a centralized platform for campus information.
- Allow students to access their academic schedules and campus updates.
- Enable administrators to manage student and campus information.
- Provide an AI chatbot for answering campus-related queries.
- Protect pages using authentication and role-based access control.
- Store and retrieve information using a MySQL database.

## 3. Key Features

### Student Features
- Student login and personalized dashboard.
- View class timetable and schedule.
- Access campus notices.
- View upcoming events.
- Ask questions through the AI chatbot.

### Administrator Features
- Secure administrator login.
- Admin dashboard.
- Student management.
- Faculty management.
- Notice management.
- Timetable management.
- Event management.
- Access to relevant campus information.

### AI Chatbot
- Answers campus-related questions.
- Uses available campus information from the database.
- Integrates with Google Gemini AI.
- Includes input validation and a fallback mechanism for certain AI service errors.

### Security and Reliability
- Password hashing.
- Login-required routes.
- Role-based access restrictions.
- Automated application tests.
- MySQL database backup and restore testing.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Database management |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive layout |
| JavaScript | Client-side interactions |
| Google Gemini API | AI chatbot responses |
| pytest | Automated testing |
| python-dotenv | Environment configuration |

## 5. Project Structure

The main project directory is:

`D:\CAMPUS AI ASSISTANT`

Important files and directories include:

- `app.py` — Flask application and routes.
- `database.py` — Database connection utilities.
- `config.py` — Application configuration.
- `.env` — Local environment variables and secrets.
- `.venv/` — Python virtual environment.
- `templates/` — HTML templates.
- `static/` — CSS, JavaScript, and other static assets, if used.
- `tests/` — Automated tests.
- `campus_ai_backup.sql` — Database backup file, if stored in the project directory.

The exact contents may vary according to the current project files.

## 6. Requirements

Install or configure the following:

- Python 3.14, or the Python version compatible with your installed dependencies.
- MySQL Server.
- MySQL command-line tools, including `mysql` and `mysqldump`.
- A Google Gemini API key for AI functionality.
- Visual Studio Code or another code editor.

## 7. Installation and Setup

### Step 1: Open the project

Open the project folder in Visual Studio Code:

`D:\CAMPUS AI ASSISTANT`

### Step 2: Activate the virtual environment

Open the VS Code terminal and execute:

```powershell
cd "D:\CAMPUS AI ASSISTANT"
.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

If a `requirements.txt` file exists, run:

```powershell
python -m pip install -r requirements.txt
```

If it does not exist, install the packages required by the current project and its imports.

### Step 4: Configure environment variables

Create or update the local `.env` file using the variable names expected by the application.

Example:

```dotenv
FLASK_SECRET_KEY=replace_with_a_random_secret
GEMINI_API_KEY=replace_with_your_api_key
GEMINI_MODEL=your_configured_gemini_model
```

Use the Gemini model configured for your application. Never commit `.env` or expose API keys, database passwords, or other secrets.

### Step 5: Configure MySQL

Ensure MySQL Server is running and the application database is configured as:

`campus_ai`

Create or restore the required tables using your project's existing database setup and backup procedures. Configure database credentials locally according to `database.py` and `config.py`.

### Step 6: Run the application

```powershell
python app.py
```

Open the local address shown in the terminal, normally:

http://127.0.0.1:5000

Log in using your existing authorized administrator or student account.

## 8. Database

The project uses MySQL database `campus_ai`.

The database includes tables for core campus information, such as:

- `users`
- `students`
- `departments`
- `faculty`
- `notices`
- `subjects`
- `timetable`
- `events`
- `chat_history`
- `documents`
- `campus_info`

The actual schema should be verified against the current database.

## 9. Database Backup and Restore

A database backup has been created and the restore process has been tested using a separate database named `campus_ai_restore_test`.

### Create a backup

```powershell
mysqldump -u root -p campus_ai --result-file="D:\CAMPUS AI ASSISTANT\campus_ai_backup.sql"
```

### Restore into a separate test database

First create the test database in MySQL:

```sql
CREATE DATABASE campus_ai_restore_test;
```

Then execute this command in PowerShell:

```powershell
mysql -u root -p campus_ai_restore_test < "D:\CAMPUS AI ASSISTANT\campus_ai_backup.sql"
```

Verify the restored tables and record counts before considering the backup fully validated.

**Important:** Keep the original `campus_ai` database safe. Do not restore over the production or working database during a test.

## 10. Testing

The project has previously reported 22 passing automated tests.

Tests cover areas including:

- Chatbot request validation.
- Chatbot response handling.
- Authentication requirements.
- Role-based access restrictions.
- Protection of administrator and student routes.

Run the tests from the project directory:

```powershell
python -m pytest -v
```

Review the latest test output before reporting the final test count.

## 11. Security Considerations

- Store passwords as secure hashes, not plaintext.
- Keep API keys and Flask secret keys out of source control.
- Restrict administrator routes to authorized administrators.
- Validate user input on the server.
- Use parameterized SQL queries.
- Keep backups in a secure location.
- Do not commit real student records or sensitive database dumps to a public repository.

## 12. Future Scope

Possible future improvements include:

- Better chatbot context retrieval.
- More advanced timetable filtering.
- Student attendance tracking.
- Assignment and examination information.
- Email or notification integration.
- Analytics and reporting.
- Deployment to a secure hosting platform.

These are potential future enhancements and are not necessarily implemented in the current version.

## 13. Conclusion

Campus AI Assistant provides a centralized platform for student information, academic schedules, campus announcements, administrative management, and AI-assisted campus queries.

By combining Flask, MySQL, and Google Gemini AI, the project demonstrates web development, database integration, authentication, access control, and AI integration in a practical campus application.

---

**Project Name:** Campus AI Assistant  
**Backend:** Python and Flask  
**Database:** MySQL  
**AI Integration:** Google Gemini  
**Development Environment:** Visual Studio Code  
**Project Status:** Core application features implemented; verify current tests and deployment requirements before release.