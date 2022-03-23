from django import template
from flags.models import *
from flags.views import *
from redFlags.urls import router
from flags.models import *

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


# @register.simple_tag()
# def get_tender(tender_id):
#     return Tender.objects.get(pk=tender_id)


@register.simple_tag()
def get_entity(entity_id):
    return Entity.objects.get(pk=entity_id)


@register.simple_tag()
def get_flags(tender_id):
    return Flag.objects.filter(tender=tender_id)


@register.simple_tag()
def flags_num(flag_query):
    return len(set([x.name for x in flag_query]))


@register.simple_tag()
def get_all_tenders():
    return Tender.object.all()