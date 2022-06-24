from django import template
from flags.models import *
from flags.flags_descriptions import flags_descriptions

register = template.Library()


@register.simple_tag()
def get_all_entities():
    return Entity.objects.all()


@register.simple_tag()
def get_flag_types():
    return Irregularity.objects.all()


@register.filter()
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag()
def get_flag_description(irregularity_id):
    return flags_descriptions.get(irregularity_id)
