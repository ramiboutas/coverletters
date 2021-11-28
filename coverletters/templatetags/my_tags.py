from django import template
register = template.Library()

from coverletters.models import Item

@register.simple_tag
def get_item_name(row, column):
    try:
        item = Item.objects.get(row=row, column=column)
    except:
        return ""
    return item.name
