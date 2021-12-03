import uuid

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.urls import reverse, reverse_lazy
from django.dispatch import receiver

from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

DEFAULT_HASHTAGS = ['#recluiter_name', '#company_name', '#street_and_number', '#zipcode_city', '#job_position']
DEFAULT_NUMBER_OF_ROWS = 3

class CoverLetter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(Session, related_name='coverletters', on_delete=models.CASCADE)

    candidate_name = models.CharField(max_length=50, blank=True, null=True)
    candidate_position = models.CharField(max_length=50, blank=True, null=True)
    candidate_email = models.EmailField(max_length=100, blank=True, null=True)
    candidate_phone = models.CharField(max_length=15, blank=True, null=True)
    candidate_location = models.CharField(max_length=25, blank=True, null=True)
    candidate_website = models.URLField(max_length=100, blank=True, null=True)

    company_text = models.TextField() #body text

    location_date = models.CharField(max_length=50, blank=True, null=True)
    applying_position = models.CharField(max_length=200, blank=True, null=True)

    text = models.TextField() #body text

    max_of_rows = models.SmallIntegerField(default=12)
    max_of_columns = models.SmallIntegerField(default=10)
    created_on = models.DateField(auto_now=True)

    def number_of_columns(self):
        return self.columns.count()

    def number_of_rows(self):
        return self.rows.count()

    def get_absolute_url(self):
        return reverse('coverletters_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('coverletters_update', kwargs={'pk':self.pk})

    def save_text_dynamic_url(self):
        return reverse('coverletters_hx_save_text_dynamic_url', kwargs={'pk':self.pk})

    def save_company_text_dynamic_url(self):
        return reverse('coverletters_hx_save_company_text_dynamic_url', kwargs={'pk':self.pk})

    def save_candidate_info_dynamic_url(self):
        return reverse('coverletters_hx_save_candidate_info_dynamic_url', kwargs={'pk':self.pk})

    def save_applying_position_dynamic_url(self):
        return reverse('coverletters_hx_save_applying_position_dynamic_url', kwargs={'pk':self.pk})

    def save_location_date_dynamic_url(self):
        return reverse('coverletters_hx_save_location_date_dynamic_url', kwargs={'pk':self.pk})

    def add_table_row_url(self):
        return reverse('coverletters_hx_add_table_row_url', kwargs={'pk':self.pk})

    def add_table_column_url(self):
        return reverse('coverletters_hx_add_table_column_url', kwargs={'pk':self.pk})

    def download_all_rows_url(self):
        return reverse('texfiles_download_all_rows_url', kwargs={'pk':self.pk})

class Row(models.Model):
    coverletter = models.ForeignKey(CoverLetter, related_name='rows', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.position}"

    def delete_url(self):
        return reverse('coverletters_hx_delete_table_row_url', kwargs={'pk':self.pk, 'pk_parent':self.coverletter.pk})

class Column(models.Model):
    coverletter = models.ForeignKey(CoverLetter, related_name='columns', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

    def delete_url(self):
        return reverse('coverletters_hx_delete_table_column_url', kwargs={'pk':self.pk, 'pk_parent':self.coverletter.pk})


class Hashtag(models.Model):
    column = models.OneToOneField(Column, related_name='hashtag', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    def save_url(self):
        return reverse('coverletters_hx_save_hashtag_url', kwargs={'pk':self.pk, 'pk_column':self.column.pk})


class Item(models.Model):
    column = models.ForeignKey(Column, related_name='items', on_delete=models.CASCADE)
    row = models.ForeignKey(Row, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def save_url(self):
        return reverse('coverletters_hx_save_item_url', kwargs={'pk':self.pk, 'pk_parent':self.hashtag.pk})


@receiver(post_save, sender=CoverLetter)
def create_rows(sender, instance, created, **kwargs):
    if created:
        objects = []
        for item in range(DEFAULT_NUMBER_OF_ROWS):
             # Row.objects.create(coverletter=instance)
            objects.append(Row(coverletter=instance))
        Row.objects.bulk_create(objects)


@receiver(post_save, sender=CoverLetter)
def create_default_columns_and_hashtags(sender, instance, created, **kwargs):
    if created:
        objects = []
        for hashtag in DEFAULT_HASHTAGS:
            column = Column(coverletter=instance)
            column.save()
            objects.append(Hashtag(column=column, name=hashtag))
        Hashtag.objects.bulk_create(objects)
