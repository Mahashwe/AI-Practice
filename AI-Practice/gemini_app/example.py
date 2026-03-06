"""
Example usage of the Gemini LLM integration.

Run this from the Django project root with:
    python manage.py shell < gemini_app/example.py
"""

from gemini_app.views import call_gemini_api

# Example 1: Simple query
print("Example 1: Asking a simple question")
print("=" * 50)
prompt1 = "What is Python and what is it used for?"
response1 = call_gemini_api(prompt1)
print(f"Prompt: {prompt1}")
print(f"Response: {response1}\n")

# Example 2: Code generation
print("\nExample 2: Asking for code")
print("=" * 50)
prompt2 = "Write a Python function that reverses a string"
response2 = call_gemini_api(prompt2)
print(f"Prompt: {prompt2}")
print(f"Response: {response2}\n")

# Example 3: Creative writing
print("\nExample 3: Creative prompt")
print("=" * 50)
prompt3 = "Write a short poem about artificial intelligence"
response3 = call_gemini_api(prompt3)
print(f"Prompt: {prompt3}")
print(f"Response: {response3}\n")
