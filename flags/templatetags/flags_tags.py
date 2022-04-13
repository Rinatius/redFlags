from django import template
from flags.models import *
from flags.views import *
from redFlags.urls import router
from flags.models import *
from datetime import datetime

register = template.Library()


@register.simple_tag()
def get_urls():
    return router.get_routes(TenderViewSet)


@register.simple_tag()
def get_inn(id, a, b):
    # return id.replace('KG-INN-', '')
    return id.replace(a, b)


@register.simple_tag()
def get_lot(lot_id):
    return Lot.objects.get(pk=lot_id)


@register.simple_tag()
def get_entity(entity_id):
    return Entity.objects.get(pk=entity_id)


@register.simple_tag()
def get_flags(tender_id):
    return Flag.objects.filter(tender=tender_id)


@register.simple_tag()
def flags_num(flag_query):
    flag_len = len(set([x.name for x in flag_query]))
    flag_icons = '🚩' * flag_len
    return flag_icons


@register.simple_tag()
def get_all_tenders():
    return Tender.object.all()


@register.simple_tag()
def get_all_entities():
    return Entity.objects.all()


@register.simple_tag()
def split_description(description):
    return description.split(' - ')


@register.simple_tag()
def check_type(x):
    return type(x)


@register.simple_tag()
def format_datetime(str_date):
    obj_date = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%fZ')
    # obj_date = obj_date.strftime('%Y')
    return obj_date


@register.simple_tag()
def flags_dict(flag_query):
    flag_dict = {flag.name: [] for flag in flag_query}

    for flag in flag_query:
        flag_dict[flag.name].append(flag)

    return flag_dict


@register.simple_tag()
def lot_list(lot):
    # return [[x.name, x.description, x.price] for x in lot]
    return lot


@register.simple_tag()
def get_len(x):
    return len(x)