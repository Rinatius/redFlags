from django import template
from flags.models import *

register = template.Library()


@register.simple_tag()
def get_all_entities():
    return Entity.objects.all()


@register.simple_tag()
def get_flag_types():
    return Irregularity.objects.all()
