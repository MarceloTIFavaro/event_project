from django.contrib import admin
from .models import events

@admin.register(events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name_event', 'creator', 'date_event', 'created_at')
    search_fields = ('name_event', 'creator__first_name', 'creator__last_name')
