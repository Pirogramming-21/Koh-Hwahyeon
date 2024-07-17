from django.contrib import admin
from .models import Idea, IdeaStar

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'interest', 'tool')
    search_fields = ('title',)
    list_filter = ('tool',)

class IdeaStarAdmin(admin.ModelAdmin):
    list_display = ('idea', 'created_at')
    search_fields = ('idea__title',)

admin.site.register(Idea, IdeaAdmin)
admin.site.register(IdeaStar, IdeaStarAdmin)