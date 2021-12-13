from django.conf import settings

from texfiles.models import TexFile


def coverletters(request):
    return {
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'texfiles': TexFile.objects.filter(is_active=True),
        'request': request
    }
