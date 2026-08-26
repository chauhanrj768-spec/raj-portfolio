from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ('__str__', 'photo_preview', 'updated_at')
    readonly_fields = ('photo_preview', 'updated_at')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" height="80" style="border-radius:50%;object-fit:cover;" />', obj.photo.url)
        return '(no photo)'
    photo_preview.short_description = 'Preview'

    def has_add_permission(self, request):
        # Only allow one profile row
        return not Profile.objects.exists()


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display   = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter    = ('is_read', 'created_at')
    search_fields  = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_editable  = ('is_read',)
    ordering       = ('-created_at',)
