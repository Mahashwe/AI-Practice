# Gemini LLM Django App

This Django app integrates with Google's Gemini API to provide LLM capabilities.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your Gemini API Key:**
   Create a `.env` file in the project root or set the environment variable:
   ```bash
   set GEMINI_API_KEY=your_api_key_here
   ```
   
   Get your API key from: https://aistudio.google.com/apikey

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

### Main Function: `call_gemini_api(prompt)`

Located in `gemini_app/views.py`, this function:
- Takes a text prompt as input
- Calls the Gemini 2.0 Flash model
- Returns the generated text response
- Uses your Gemini API key from environment variables

**Example:**
```python
from gemini_app.views import call_gemini_api

response = call_gemini_api("What is Python programming?")
print(response)
```

### API Endpoint: `/api/query/`

**GET Request:**
```
GET http://localhost:8000/api/query/
```
Returns endpoint information.

**POST Request:**
```bash
curl -X POST http://localhost:8000/api/query/ \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is machine learning?"}'
```

**Response:**
```json
{
    "prompt": "What is machine learning?",
    "response": "Machine learning is...",
    "model": "gemini-2.0-flash",
    "query_id": 1
}
```

## Model Information

- **Model Name:** `gemini-2.0-flash`
- **Type:** Fast, efficient multimodal model
- **Use Case:** Real-time LLM applications

## Database

The app stores queries in the `GeminiQuery` model with:
- `prompt`: The input prompt
- `response`: The API response
- `created_at`: Timestamp of the query

View stored queries in the Django admin at `/admin/`
