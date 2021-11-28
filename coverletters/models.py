from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.urls import reverse, reverse_lazy
from django.dispatch import receiver

DEFAULT_HASHTAGS = ['#address', '#name', '#charge', '#company']
DEFAULT_NUMBER_OF_ITEMS = 5

class CoverLetter(models.Model):
    text = models.TextField()
    number_of_item_rows = models.SmallIntegerField(default=DEFAULT_NUMBER_OF_ITEMS)
    max_item_rows = models.SmallIntegerField(default=12) # maybe for premium -> 25, for free -> 5
    max_hastags = models.SmallIntegerField(default=10) # maybe for premium -> 10, for free -> 5

    def number_of_hashtags(self):
        return self.hashtags.count()

    def list_of_rows(self):
        return range(self.number_of_item_rows)

    def get_absolute_url(self):
        return reverse('coverletters_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('coverletters_update', kwargs={'pk':self.pk})

    def save_text_dynamic_url(self):
        return reverse('coverletters_hx_save_text_dynamic_url', kwargs={'pk':self.pk})

    def add_table_row_url(self):
        return reverse('coverletters_hx_add_row_url', kwargs={'pk':self.pk})

    def add_table_column_url(self):
        return reverse('coverletters_hx_add_table_column_url', kwargs={'pk':self.pk})



class Hashtag(models.Model):
    coverletter = models.ForeignKey(CoverLetter, related_name='hashtags', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    def save_url(self):
        return reverse('coverletters_hx_save_hashtag_url', kwargs={'pk':self.pk, 'pk_parent':self.coverletter.pk})



class Item(models.Model):
    hashtag = models.ForeignKey(Hashtag, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    row_position = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=CoverLetter)
def create_default_hashtags(sender, instance, created, **kwargs):
    if created:
        objects = []
        for hashtag in DEFAULT_HASHTAGS:
            objects.append(Hashtag(coverletter=instance, name=hashtag))
        Hashtag.objects.bulk_create(objects)
