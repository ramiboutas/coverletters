from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.urls import reverse, reverse_lazy
from django.dispatch import receiver

DEFAULT_HASHTAGS = ['#address', '#name', '#charge', '#company']
DEFAULT_NUMBER_OF_ROWS = 3

class CoverLetter(models.Model):
    text = models.TextField()
    number_of_item_rows = models.SmallIntegerField(default=5)
    max_of_rows = models.SmallIntegerField(default=12) # maybe for premium -> 25, for free -> 5
    max_of_columns = models.SmallIntegerField(default=10) # maybe for premium -> 10, for free -> 5

    def number_of_columns(self):
        return self.columns.count()

    def list_of_rows(self):
        return range(self.number_of_item_rows)

    def get_absolute_url(self):
        return reverse('coverletters_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('coverletters_update', kwargs={'pk':self.pk})

    def save_text_dynamic_url(self):
        return reverse('coverletters_hx_save_text_dynamic_url', kwargs={'pk':self.pk})

    def add_table_row_url(self):
        return reverse('coverletters_hx_add_table_row_url', kwargs={'pk':self.pk})

    def add_table_column_url(self):
        return reverse('coverletters_hx_add_table_column_url', kwargs={'pk':self.pk})


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
    row_position = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.name

    def save_url(self):
        return reverse('coverletters_hx_save_item_url', kwargs={'pk':self.pk, 'pk_parent':self.hashtag.pk})


@receiver(post_save, sender=CoverLetter)
def create_rows(sender, instance, created, **kwargs):
    if created:
        objects = []
        for item in range(DEFAULT_NUMBER_OF_ROWS):
            row = Row(coverletter=instance)
            row.save()


@receiver(post_save, sender=CoverLetter)
def create_default_columns_and_hashtags(sender, instance, created, **kwargs):
    if created:
        objects = []
        for hashtag in DEFAULT_HASHTAGS:
            column = Column(coverletter=instance)
            column.save()
            objects.append(Hashtag(column=column, name=hashtag))
        Hashtag.objects.bulk_create(objects)


# not working! check on goole: Singal for multiple senders django
# @receiver(post_save, sender=Row)
# @receiver(post_save, sender=Column)
# def create_default_items(sender, instance, created, **kwargs):
#     item = Item(name="new item", row=Row(), column=Column())
#     item.save()
#     if created:
#         if sender.__name__ == 'Row':
#             item.row = instance
#         else:
#             # item = Item.objects.get(id=id)
#             item.column = instance
#         item.save()





    # objects = []
    # for item in range(DEFAULT_NUMBER_OF_ITEMS):
    #     objects.append(Item(hashtag=instance, name=f"item {item}"))
    # Item.objects.bulk_create(objects)
