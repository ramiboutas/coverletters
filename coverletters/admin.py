from django.contrib import admin

from .models import CoverLetter, Hashtag, Item, Row, Column
from django.contrib.sessions.models import Session



class CoverLetterAdmin(admin.ModelAdmin):
    readonly_fields = ['session', 'created_on', 'zip_file', 'tex_file']
    list_display = ['pk', 'candidate_name', 'created_on' ]

admin.site.register(CoverLetter, CoverLetterAdmin)
