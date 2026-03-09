# 🧠 AI Therapist Chatbot

A compassionate AI-powered therapist chatbot built with Django and Streamlit, powered by Google's Gemini 2.0 Flash model.

## 📋 Overview

This project combines a Django backend API with a Streamlit frontend to create an accessible, AI-assisted therapy conversation platform. Users can chat with an empathetic AI therapist trained to provide support, active listening, and practical coping strategies.

**⚠️ Important Disclaimer:** This is an AI-assisted conversation tool for emotional support and guidance only. It is NOT a replacement for professional mental health treatment. For serious mental health concerns, please consult a licensed therapist or mental health professional.

## ✨ Features

- **Active Listening:** The AI therapist listens carefully to user concerns
- **Empathetic Responses:** Compassionate and non-judgmental communication
- **Coping Strategies:** Practical advice based on CBT and mindfulness principles
- **Chat History:** All conversations are saved locally for reference
- **Real-time Responses:** Fast, streaming responses powered by Gemini 2.0 Flash
- **Professional Guidelines:** Responses follow therapeutic best practices
- **Clean UI:** User-friendly Streamlit interface with message history

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                       │
│                    (Port 8501)                              │
│  - Chat interface with therapist persona                    │
│  - Message history & statistics                             │
│  - System prompt injection for therapeutic behavior         │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP POST /api/query/
                     ↓
┌─────────────────────────────────────────────────────────────┐
│                   Django Backend                             │
│                   (Port 8000)                                │
│  - REST API endpoint at /api/query/                          │
│  - Gemini API integration with system instructions           │
│  - SQLite database for query persistence                     │
│  - Django admin interface at /admin/                         │
└────────────────────┬────────────────────────────────────────┘
                     │ 
                     ↓
┌─────────────────────────────────────────────────────────────┐
│              Google Gemini 2.0 Flash API                     │
│              (Cloud-hosted LLM)                              │
└─────────────────────────────────────────────────────────────┘
```

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

**Terminal 1 - Start Django Backend:**
```bash
cd AI-Practice
python manage.py runserver
```
Backend will be available at `http://localhost:8000`

**Terminal 2 - Start Streamlit Frontend:**
```bash
streamlit run streamlit_app.py
```
Frontend will be available at `http://localhost:8501`

## 📖 How to Use

1. Open your browser to `http://localhost:8501`
2. Type your message or concern in the input field
3. Press "Send" and wait for the therapist's response
4. Continue the conversation naturally
5. Use "Clear Chat History" in the sidebar to start fresh
6. Adjust the API endpoint in settings if needed

### Example Conversations

**Example 1 - Anxiety Support:**
```
User: I'm feeling really anxious about my job interview tomorrow
Therapist: That's completely understandable - job interviews can feel nerve-wracking. 
Can you tell me more about what specifically makes you anxious? Is it about the questions 
they might ask, or something else?
```

**Example 2 - Stress Management:**
```
User: Work has been overwhelming lately. I don't know how to manage everything
Therapist: It sounds like you're carrying a lot right now. Let's break this down together.
What are the top 3 things that are making you feel most overwhelmed?
```

## 🛠️ Project Structure

```
project/
├── streamlit_app.py              # Main Streamlit chat interface
├── requirements.txt              # Python dependencies
├── THERAPIST_CHATBOT_README.md   # This file
├── GEMINI_APP_README.md          # Django app documentation
├── STREAMLIT_GUIDE.md            # Streamlit setup guide
└── AI-Practice/
    ├── manage.py                 # Django management
    ├── main.py                   # Entry point (empty)
    ├── mysite/                   # Django project settings
    │   ├── settings.py           # Django configuration
    │   ├── urls.py               # URL routing
    │   └── wsgi.py               # WSGI configuration
    └── gemini_app/               # Therapist chatbot application
        ├── models.py             # GeminiQuery database model
        ├── views.py              # API endpoint & Gemini integration
        ├── urls.py               # App URL patterns
        ├── admin.py              # Django admin configuration
        ├── apps.py               # App configuration
        └── example.py            # Usage examples
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

| Technology | Version | Purpose |
|-----------|---------|---------|
| Django | 5.2.11 | Backend web framework |
| Streamlit | 1.31.0 | Frontend chat interface |
| google-generativeai | 0.7.2 | Gemini API client |
| requests | 2.31.0 | HTTP client library |
| SQLite | Built-in | Database |

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
- **Solution:** Make sure Django is running on Terminal 1 at `http://localhost:8000`

### Issue: "GEMINI_API_KEY environment variable not set"
- **Solution:** Set your API key (see Installation section)

### Issue: "Request timeout"
- **Solution:** Increase timeout in streamlit_app.py or check internet connection

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

1. Update the system prompt in `streamlit_app.py` (THERAPIST_PROMPT variable)
2. Add new therapeutic approaches in the system prompt
3. Customize the UI styling in the HTML/CSS section
4. Modify the database model if needed in `gemini_app/models.py`

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
