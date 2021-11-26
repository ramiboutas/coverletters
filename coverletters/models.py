from django.db import models
from django.urls import reverse

class CoverLetter(models.Model):
    text = models.TextField()
    number_of_hashtags = models.SmallIntegerField(default=4)
    number_of_items = models.SmallIntegerField(default=1)

    def get_absolute_url(self):
        return reverse('coverletters_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('coverletters_update', kwargs={'pk':self.pk})


class Hashtag(models.Model):
    coverletter = models.ForeignKey(CoverLetter, related_name='hashtags', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):
    hashtag = models.ForeignKey(Hashtag, related_name='hashtags', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
