from django.contrib import admin

from .models import Settings, Team

# Register your models here.
admin.site.register(Settings)
admin.site.register(Team)