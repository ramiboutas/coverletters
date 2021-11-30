
from .models import TexFile


def files(request):
    return {
        'texfiles': TexFile.objects.filter(is_active=True),
        'request': request
    }
