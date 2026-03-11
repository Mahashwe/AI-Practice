# 🧠 AI Therapist Chatbot

A compassionate AI-powered therapist chatbot built with Django and powered by Google's Gemini 2.0 Flash model.

## 📋 Overview

This project provides a Django backend API for an AI-assisted therapy conversation platform. Users can chat with an empathetic AI therapist trained to provide support, active listening, and practical coping strategies. An HTML/CSS/JS frontend will be added in the next phase.

**⚠️ Important Disclaimer:** This is an AI-assisted conversation tool for emotional support and guidance only. It is NOT a replacement for professional mental health treatment. For serious mental health concerns, please consult a licensed therapist or mental health professional.

## ✨ Features

- **Active Listening:** The AI therapist listens carefully to user concerns
- **Empathetic Responses:** Compassionate and non-judgmental communication
- **Coping Strategies:** Practical advice based on CBT and mindfulness principles
- **Chat History:** All conversations are saved locally for reference
- **Real-time Responses:** Fast, streaming responses powered by Gemini 2.0 Flash
- **Professional Guidelines:** Responses follow therapeutic best practices
- **User Conversations:** Saves user conversations and extracts keywords for analysis
- **Django Admin:** Manage conversations and queries through Django admin interface

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Django Backend API                         │
│                  (Port 8000)                                 │
│  - REST API endpoint at /api/query/                          │
│  - Gemini API integration with system instructions           │
│  - SQLite database for query & conversation persistence      │
│  - Django admin interface at /admin/                         │
│  - User conversation tracking & keyword extraction           │
└────────────────────┬────────────────────────────────────────┘
                     │ 
                     ↓
┌─────────────────────────────────────────────────────────────┐
│              Google Gemini 2.0 Flash API                     │
│              (Cloud-hosted LLM)                              │
└─────────────────────────────────────────────────────────────┘
```

**Frontend Coming Next:** HTML/CSS/JavaScript interface will be added to interact with this API.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API Key (free from https://aistudio.google.com/apikey)
- pip (Python package manager)

### Installation

1. **Clone or download the project:**
   ```bash
   cd path/to/project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API Key:**
   - On Windows (PowerShell):
     ```powershell
     $env:GEMINI_API_KEY = "your-api-key-here"
     ```
   - On Windows (Command Prompt):
     ```cmd
     set GEMINI_API_KEY=your-api-key-here
     ```
   - On Linux/Mac:
     ```bash
     export GEMINI_API_KEY="your-api-key-here"
     ```

4. **Run Django migrations:**
   ```bash
   cd AI-Practice
   python manage.py migrate
   ```

### Running the Application

**Start Django Backend:**
```bash
cd AI-Practice
python manage.py runserver
```
Backend will be available at `http://localhost:8000`
Admin interface at `http://localhost:8000/admin/`

**Access API Endpoints:**
- Chat API: `POST http://localhost:8000/api/query/`
- Admin Panel: `http://localhost:8000/admin/`

**Note:** Frontend is under development. Currently, test the API using curl or Postman.

## 📖 How to Use the API

### Test with Postman or curl:

**Example 1 - Basic Query:**
```bash
curl -X POST http://localhost:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "I'm feeling anxious about my job interview",
    "user_id": 1
  }'
```

**Example 2 - With Custom System Prompt:**
```bash
curl -X POST http://localhost:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "I'm feeling overwhelmed",
    "system_prompt": "You are a compassionate therapist",
    "user_id": 1
  }'
```

### View Conversations in Django Admin:
1. Go to `http://localhost:8000/admin/`
2. Login with admin credentials
3. Click on **User Conversations** to view all saved conversations
4. Search by username or keywords

## 🛠️ Project Structure

```
project/
├── requirements.txt              # Python dependencies
├── THERAPIST_CHATBOT_README.md   # This file
├── GEMINI_APP_README.md          # Django app documentation
└── AI-Practice/
    ├── manage.py                 # Django management
    ├── main.py                   # Entry point (empty)
    ├── mysite/                   # Django project settings
    │   ├── settings.py           # Django configuration
    │   ├── urls.py               # URL routing
    │   └── wsgi.py               # WSGI configuration
    ├── db.sqlite3                # SQLite database
    └── gemini_app/               # Therapist chatbot application
        ├── models.py             # GeminiQuery & UserConversation models
        ├── views.py              # API endpoint & Gemini integration
        ├── urls.py               # App URL patterns
        ├── admin.py              # Django admin configuration
        ├── apps.py               # App configuration
        └── migrations/           # Database migrations
```

## 📊 Therapist System Prompt

The AI is guided by the following system prompt to ensure therapeutic behavior:

```
You are a compassionate and professional therapist with expertise in cognitive 
behavioral therapy, mindfulness-based approaches, and emotional support.

Guidelines:
- Listen actively and validate the user's feelings
- Ask thoughtful clarifying questions
- Provide supportive and non-judgmental responses
- Offer practical coping strategies
- Encourage self-reflection and positive thinking
- Maintain appropriate professional boundaries
- Be empathetic, warm, and genuine
```

This ensures consistent, empathetic responses across all conversations.

## 💾 Database

Conversations are stored in SQLite with the following fields:

| Field | Type | Purpose |
|-------|------|---------|
| prompt | Text | User's message |
| response | Text | Therapist's response |
| created_at | DateTime | When the query was made |

Access the database through Django Admin:
- URL: `http://localhost:8000/admin/`
- Default credentials: username=`admin`, password=`admin` (for development)

## 📚 Technologies Used

The AI is guided by a therapeutic system prompt to ensure compassionate, professional responses.

## 📱 Database Models

### GeminiQuery
Store individual queries and responses:
- `prompt`: User's message
- `response`: AI's response  
- `created_at`: Timestamp

### UserConversation (New)
Store user conversations with keyword extraction:
- `user`: Foreign key to User
- `conversation`: Full conversation text
- `keywords`: Extracted keywords
- `created_at`: When conversation started
- `updated_at`: Last update time

## 📚 Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| Django | 5.2.11 | Backend web framework |
| google-generativeai | 0.7.2 | Gemini API client |
| requests | 2.31.0 | HTTP client library |
| SQLite | Built-in | Database |
| HTML/CSS/JS | Coming | Frontend interface (in progress) |

## 🔒 Security & Privacy Notes

### Current State (Development)
- ⚠️ DEBUG=True (disable for production)
- ⚠️ SECRET_KEY exposed in settings (use environment variables)
- ⚠️ ALLOWED_HOSTS empty

### For Production Deployment

1. **Environment Variables:**
   ```python
   # settings.py
   SECRET_KEY = os.getenv('SECRET_KEY')
   DEBUG = os.getenv('DEBUG', 'False') == 'True'
   ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
   ```

2. **HTTPS/SSL:** Deploy with HTTPS only

3. **CORS:** Add `django-cors-headers` for cross-origin requests

4. **Data Privacy:** Store conversations securely; consider encryption

5. **Rate Limiting:** Add DRF throttling to prevent abuse

## 🐛 Troubleshooting

### Issue: "Cannot connect to Django API"
- **Solution:** Make sure Django is running at `http://localhost:8000`
- Run: `python manage.py runserver`

### Issue: "GEMINI_API_KEY environment variable not set"
- **Solution:** Set your API key (see Installation section)

### Issue: "User with id not found"
- **Solution:** Create users in Django admin first or query without user_id

### Issue: "Database locked"
- **Solution:** Close all connections and ensure only one Django instance is running

## 📝 Example API Requests

### Using curl:
```bash
curl -X POST http://localhost:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "I am feeling anxious",
    "system_prompt": "Act as a supportive therapist"
  }'
```

### Using Python requests:
```python
import requests

payload = {
    "prompt": "I am feeling anxious",
    "system_prompt": "Act as a supportive therapist"
}

response = requests.post('http://localhost:8000/api/query/', json=payload)
print(response.json())
```

## 🤝 Contributing

To modify or extend this project:

1. Update the system prompt in `gemini_app/views.py` or via API parameter
2. Add new therapeutic approaches in the system prompt
3. Customize the Django models in `gemini_app/models.py` as needed
4. Frontend will be added using HTML/CSS/JavaScript

## 🔜 Next Steps

- [ ] Build HTML/CSS/JavaScript frontend
- [ ] Add user authentication
- [ ] Implement conversation filtering and search
- [ ] Add analytics dashboard
- [ ] Production deployment setup

## 📄 License

This project is provided as-is for educational purposes.

## ⚕️ Mental Health Resources

If you or someone you know is struggling with mental health:

- **National Crisis Hotline:** 988 (US)
- **Crisis Text Line:** Text HOME to 741741
- **International Association for Suicide Prevention:** https://www.iasp.info/resources/Crisis_Centres/
- **SAMHSA National Helpline:** 1-800-662-4357 (free, confidential, 24/7)

Remember: This chatbot is a tool for support, not a replacement for professional mental health care.

## ❓ FAQ

**Q: Can I use this for commercial purposes?**
A: This is for educational use. Consult licensing requirements for commercial deployment.

**Q: How accurate is the therapist?**
A: It's an AI model trained on general therapeutic principles. A licensed therapist is always preferable.

**Q: Where are my conversations stored?**
A: Locally in SQLite database (db.sqlite3). Always be cautious with sensitive information.

**Q: Can I customize the therapist's behavior?**
A: Yes! Modify the THERAPIST_PROMPT in streamlit_app.py to adjust responses.

**Q: What if the therapist gives harmful advice?**
A: Stop immediately and consult a licensed mental health professional.

---

**Last Updated:** March 2026  
**Status:** Fully Functional
