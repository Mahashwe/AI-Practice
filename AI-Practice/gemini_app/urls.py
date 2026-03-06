from django.urls import path
from . import views

app_name = 'gemini_app'

urlpatterns = [
    path('query/', views.llm_query, name='llm_query'),
]
