# 🎓 Campus AI Assistant

An AI-powered College Management and Information Assistant built using **Python, Flask, MySQL-compatible TiDB Cloud, and Google Gemini AI**. The platform helps students and administrators access campus information, manage academic activities, and interact with an AI-powered chatbot.

## 🌐 Live Demo

**Live Website:** https://campus-ai-assistant-04.vercel.app/

**GitHub Repository:** https://github.com/divyanshsrivastav29/Campus-AI-Assistant

---

## 📌 Project Overview

Campus AI Assistant is a web-based application designed to simplify communication between students and college administration.

It provides a centralized platform for accessing academic information, managing student and faculty records, viewing notices and timetables, and interacting with an AI chatbot.

The application supports different user roles, including administrators and students, with role-based access to relevant features.

## ✨ Key Features

### 👨‍💼 Admin Module
- Admin login and authentication.
- Admin dashboard.
- Add, view, and manage student records.
- Manage faculty information.
- Publish and manage college notices.
- Manage academic timetable.
- Manage campus events.
- Manage departments and academic information.

### 🎓 Student Module
- Student login and authentication.
- Student dashboard.
- View college notices.
- View faculty information.
- Access academic timetable.
- View upcoming campus events.
- Interact with the Campus AI chatbot.

### 🤖 AI Chatbot
- Powered by Google Gemini AI.
- Answers academic and campus-related questions.
- Uses verified campus information from the database.
- Provides helpful and conversational responses.
- Includes fallback handling for temporary AI service failures.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| TiDB Cloud | MySQL-compatible cloud database |
| MySQL Connector | Database connectivity |
| Google Gemini API | AI chatbot |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactivity |
| Jinja2 | Dynamic templates |
| Vercel | Application hosting |
| Git & GitHub | Version control |

## 🏗️ System Architecture

```text
              Students / Admin
                     |
                     v
               Vercel Hosting
                     |
                     v
                Flask Backend
                /           \
               v             v
        TiDB Cloud       Gemini API
        Database         AI Chatbot
               \             /
                \           /
                 v         v
                 Campus AI
                 Assistant
```

## 📂 Project Structure

```text
CAMPUS AI ASSISTANT/
│
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── .python-version
├── .gitignore
├── ca.pem
├── README.md
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
└── tests/
```

## ⚙️ Local Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/divyanshsrivastav29/Campus-AI-Assistant.git
```

### 2. Open the Project Directory

```bash
cd "Campus-AI-Assistant"
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following configuration:

```env
FLASK_SECRET_KEY=your_secret_key

DB_HOST=your_tidb_host
DB_PORT=4000
DB_USER=your_tidb_username
DB_PASSWORD=your_tidb_password
DB_NAME=campus_ai

GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

**Important:**
- Replace placeholder values with your own credentials.
- Never upload your `.env` file to GitHub.
- Keep your API keys and database credentials private.
- Configure the TiDB CA certificate (`ca.pem`) as required by the database connection.

### 7. Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## ☁️ Deployment Architecture

The application uses the following cloud services:

| Service | Responsibility |
|---|---|
| Vercel | Hosts the Flask application |
| TiDB Cloud Starter | Stores application data |
| Google Gemini API | Provides AI chatbot functionality |
| GitHub | Stores and manages source code |

### Environment Variables on Vercel

Configure these variables under:

**Vercel Dashboard → Project → Settings → Environment Variables**

| Variable | Description |
|---|---|
| FLASK_SECRET_KEY | Flask session security |
| DB_HOST | TiDB hostname |
| DB_PORT | TiDB port |
| DB_USER | TiDB username |
| DB_PASSWORD | TiDB password |
| DB_NAME | Database name |
| GEMINI_API_KEY | Google Gemini API key |
| GEMINI_MODEL | Gemini model name |

Do not store sensitive credentials directly in source code.

## 🗄️ Database

The project uses TiDB Cloud Starter, which is compatible with MySQL.

Database name:

```text
campus_ai
```

The database manages information related to:

- Users
- Students
- Faculty
- Departments
- Notices
- Timetable
- Events
- Subjects
- Chat history
- Campus information
- Documents

## 🔐 Security

- Environment-based configuration.
- Password hashing.
- Role-based access control.
- Session-based authentication.
- Secure database connections using SSL.
- Secret credentials excluded from GitHub.

## 🚀 Future Enhancements

- Advanced AI chatbot capabilities.
- Student attendance management.
- Assignment and examination management.
- AI-powered academic assistance.
- Email and notification integration.
- Advanced analytics dashboard.
- Mobile-friendly progressive web application.

## 🎯 Project Objective

The main objective of Campus AI Assistant is to make college information more accessible, improve communication between students and administrators, and simplify campus management through artificial intelligence.

## 👨‍💻 Developer

**Divyanshu Srivastava**

BCA Student

Institute of Technology & Management, GIDA, Gorakhpur

GitHub: [@divyanshsrivastav29](https://github.com/divyanshsrivastav29)

---

⭐ If you find this project useful, consider giving the repository a star!

**Campus AI Assistant — Making Campus Information Smarter with AI.**