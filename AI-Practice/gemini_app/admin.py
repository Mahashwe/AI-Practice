from django.contrib import admin
from .models import GeminiQuery, UserConversation


@admin.register(GeminiQuery)
class GeminiQueryAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'created_at')
    search_fields = ('prompt',)


@admin.register(UserConversation)
class UserConversationAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'get_conversation_preview')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'keywords', 'conversation')
    readonly_fields = ('created_at', 'updated_at', 'conversation')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Conversation', {
            'fields': ('conversation',)
        }),
        ('Keywords', {
            'fields': ('keywords',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_conversation_preview(self, obj):
        """Display a preview of the conversation"""
        preview = obj.conversation[:100] + '...' if len(obj.conversation) > 100 else obj.conversation
        return preview
    get_conversation_preview.short_description = 'Conversation Preview'
