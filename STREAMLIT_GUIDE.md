# Streamlit Chat Interface Setup & Usage

## Installation

Install Streamlit and dependencies:
```bash
pip install -r requirements.txt
```

Or just Streamlit:
```bash
pip install streamlit requests
```

## Running the Chat Interface

1. **Start Django server first:**
   ```bash
   cd AI-Practice
   python manage.py runserver
   ```
   (Keep this running in a separate terminal)

2. **Run Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open in browser:**
   - Streamlit will automatically open at `http://localhost:8501`
   - Or manually navigate to that URL

## Features

✨ **Chat Interface:**
- Clean, modern UI for chatting with Gemini
- Real-time message display
- User and AI message differentiation

📊 **Chat Management:**
- View chat history
- Clear chat button
- Message statistics

⚙️ **Configuration:**
- Adjustable API endpoint in sidebar
- Real-time connection testing
- Error handling with helpful messages

🎨 **User Experience:**
- Responsive design
- Typing feedback
- Loading spinners
- Color-coded messages (blue for user, gray for AI)

## How It Works

1. You type a message in Streamlit
2. Streamlit sends it to Django API at `/api/query/`
3. Django calls Gemini API
4. Gemini returns response
5. Response appears in chat

## Architecture

```
Streamlit Frontend (Port 8501)
         ↓
    HTTP POST Request
         ↓
Django Backend (Port 8000) → Gemini API → Response
         ↓
    Response Back
         ↓
Display in Chat
```

## Troubleshooting

**Connection Error?**
- Ensure Django server is running: `python manage.py runserver`
- Check API endpoint in sidebar (default: `http://localhost:8000/api/query/`)

**No response from Gemini?**
- Verify GEMINI_API_KEY is set: `set GEMINI_API_KEY=your_key`
- Check internet connection
- API key might be invalid

**Streamlit not loading?**
- Clear cache: `streamlit cache clear`
- Restart Streamlit: Ctrl+C and run again
