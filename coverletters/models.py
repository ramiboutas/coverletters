import uuid
import os

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.urls import reverse, reverse_lazy
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.utils.translation import gettext_lazy as _

from texfiles.models import TexFile
from utils.files import delete_path_file

DEFAULT_HASHTAGS = [_('#recruiter'), _('#company'), _('#street_number'), _('#zipcode_city'), _('#job_position')]
DEFAULT_NUMBER_OF_ROWS = 10


class CoverLetter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(Session, related_name='coverletters', on_delete=models.CASCADE)
    tex_file = models.ForeignKey(TexFile, blank=True, null=True, on_delete=models.SET_NULL)

    candidate_name = models.CharField(max_length=50, blank=True, null=True)
    candidate_position = models.CharField(max_length=50, blank=True, null=True)
    candidate_email = models.CharField(max_length=100, blank=True, null=True)
    candidate_phone = models.CharField(max_length=15, blank=True, null=True)
    candidate_location = models.CharField(max_length=25, blank=True, null=True)
    candidate_website = models.CharField(max_length=100, blank=True, null=True)

    company_text = models.TextField() #body text

    location_date = models.CharField(max_length=50, blank=True, null=True)
    applying_position = models.CharField(max_length=200, blank=True, null=True)

    text = models.TextField() #body text

    zip_file = models.FileField(upload_to='zipfiles/%Y/%m/%d', blank=True, null=True)

    max_of_rows = models.SmallIntegerField(default=50)
    max_of_columns = models.SmallIntegerField(default=10)
    created_date = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now = True, blank=True, null=True)

    def __str__(self):
        return f'{self.pk} {self.candidate_name}'

    def number_of_columns(self):
        return self.columns.count()

    def number_of_rows(self):
        return self.rows.count()

    def get_absolute_url(self):
        return reverse('coverletters_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('coverletters_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('coverletters_delete', kwargs={'pk':self.pk})

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

    def prepare_the_download_url(self):
        return reverse('texfiles_prepare_the_download_url', kwargs={'pk':self.pk})

    def download_the_zip_file_url(self):
        return reverse('texfiles_download_the_zip_file_url', kwargs={'pk':self.pk})


class Row(models.Model):
    coverletter = models.ForeignKey(CoverLetter, related_name='rows', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

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


@receiver(post_delete, sender=CoverLetter)
def delete_zip_file(sender, instance, **kwargs):
    if instance.zip_file:
        delete_path_file(instance.zip_file.path)
