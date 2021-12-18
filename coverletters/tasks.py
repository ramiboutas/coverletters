from celery import shared_task

from django.db.models import F
from django.utils import timezone

from .models import CoverLetter


@shared_task(bind=True)
def cleanup_unmodified_coverletters(self):
    """
    All the coverletter objects that weren't modified and were created one hour before -> will be clenned up
    """
    queryset = CoverLetter.objects.annotate(
        modification_interval = F('updated_date') - F('created_date')
        ).filter(created_date__lte=timezone.now()-timezone.timedelta(hours=1), modification_interval__lte=timezone.timedelta(seconds=0.5))
    queryset.delete()
    return "cleaned"
