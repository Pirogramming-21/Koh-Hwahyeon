from django.contrib import admin
from .models import DevTool

class DevToolAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'explain')
    search_fields = ('title', 'type')

admin.site.register(DevTool, DevToolAdmin)