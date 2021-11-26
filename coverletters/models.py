from django.db import models
from django.urls import reverse

class CoverLetter(models.Model):
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('coverletters_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('coverletters_update', kwargs={'pk':self.pk})
