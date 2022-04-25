from django import template
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


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.simple_tag()
def get_flag_types():
    return Irregularity.objects.all()
