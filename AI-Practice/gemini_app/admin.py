from django.contrib import admin
from .models import GeminiQuery


@admin.register(GeminiQuery)
class GeminiQueryAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'created_at')
    search_fields = ('prompt',)
