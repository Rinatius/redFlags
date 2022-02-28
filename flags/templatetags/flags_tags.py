from django import template
from flags.models import *
from flags.views import *
from redFlags.urls import router

register = template.Library()


@register.simple_tag()
def get_menu_items():

    # return {
    #     'Tenders': 'tenders',
    #     'Lots': 'lots',
    #     'Entities': 'entities',
    #     'Bids': 'bids',
    #     'Classifiers': 'classifiers',
    #     'Irregularities': 'irregularities',
    #     'Flags': 'flags',
    # }

    # return ['tenders', 'lots', 'entities', 'bids', 'classifiers', 'irregularities', 'flags', ]
    return [
        'tender',
        'lot',
        'entity',
        'bid',
        'classifier',
        'irregularity',
        'flag',
    ]


@register.simple_tag()
def get_urls():
    return router.get_routes(TenderViewSet)


@register.simple_tag()
def get_inn(id, a, b):
    # return id.replace('KG-INN-', '')
    return id.replace(a, b)

# @register.simple_tag()
# def get_entity_url(inn):