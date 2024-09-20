from django.contrib import admin

from .models import Settings, Team

# Register your models here.
# admin.site.register(Settings)
# admin.site.register(Team)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id']