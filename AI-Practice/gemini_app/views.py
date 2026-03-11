from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
import google.generativeai as genai
import os
from .models import GeminiQuery, UserConversation


def call_gemini_api(prompt, system_prompt=None):
    """
    Call the Gemini Flash 2.5 API with a given prompt and return the response.
    
    Args:
        prompt (str): The input prompt for the Gemini model
        system_prompt (str, optional): System instruction to guide the model's behavior
        
    Returns:
        str: The response from the Gemini API
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    
    genai.configure(api_key=api_key)
    
    # Create model with optional system instruction
    if system_prompt:
        model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=system_prompt)
    else:
        model = genai.GenerativeModel('gemini-2.0-flash')
    
    response = model.generate_content(prompt)
    
    return response.text


@require_http_methods(["GET", "POST"])
def llm_query(request):
    """
    Django view to handle LLM queries via Gemini API.
    
    GET: Shows available endpoint info
    POST: Accepts a 'prompt' parameter and returns the Gemini API response
    """
    if request.method == 'GET':
        return JsonResponse({
            'message': 'Send a POST request with a "prompt" parameter',
            'example': 'POST data: {"prompt": "What is Python?"}',
            'model': 'gemini-2.0-flash'
        })
    
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body)
            prompt = data.get('prompt')
            system_prompt = data.get('system_prompt')
            user_id = data.get('user_id')
            
            if not prompt:
                return JsonResponse({'error': 'prompt parameter is required'}, status=400)
            
            response_text = call_gemini_api(prompt, system_prompt=system_prompt)
            
            query_record = GeminiQuery.objects.create(
                prompt=prompt,
                response=response_text
            )
            
            # Save conversation with user if user_id is provided
            if user_id:
                try:
                    user = User.objects.get(id=user_id)
                    conversation_text = f"User: {prompt}\n\nAssistant: {response_text}"
                    UserConversation.objects.create(
                        user=user,
                        conversation=conversation_text
                    )
                except User.DoesNotExist:
                    return JsonResponse({'error': f'User with id {user_id} not found'}, status=400)
            
            return JsonResponse({
                'prompt': prompt,
                'response': response_text,
                'model': 'gemini-2.0-flash',
                'query_id': query_record.id
            })
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'error': f'API Error: {str(e)}'}, status=500)
