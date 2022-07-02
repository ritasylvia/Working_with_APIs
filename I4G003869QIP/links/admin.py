from django.contrib import admin

# Register your models here.
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('target_url', 'description', 'identifier', 'author', 'created_date')
    list_filter = ('identifier',)
    search_fields = ['description', 'identifier']

admin.site.register(Link, LinkAdmin)
