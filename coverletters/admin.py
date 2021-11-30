from django.contrib import admin

from .models import CoverLetter, Hashtag, Item, Row, Column
from django.contrib.sessions.models import Session

admin.site.register(CoverLetter)
admin.site.register(Row)
admin.site.register(Column)
admin.site.register(Hashtag)
admin.site.register(Item)
admin.site.register(Session)
