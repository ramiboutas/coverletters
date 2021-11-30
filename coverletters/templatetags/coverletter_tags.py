from django import template
register = template.Library()

from coverletters.models import Item

@register.simple_tag
def get_item_name(row, column):
    try:
        return Item.objects.get(row=row, column=column).name
    except:
        return ""
