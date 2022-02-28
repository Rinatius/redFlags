from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework_bulk import BulkModelViewSet

from flags.models import Entity, Tender, Lot, Classifier, Bid, Irregularity, Flag
from flags.permissions import MainAccessPolicy
from flags.serializer import TenderSerializer, LotSerializer, EntitySerializer, ClassifierSerializer, BidSerializer, \
    IrregularitySerializer, FlagSerializer, FlagDataSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TenderViewSet(viewsets.ModelViewSet):
    serializer_class = TenderSerializer
    permission_classes = (MainAccessPolicy,)
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    pagination_class = CustomPagination

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Tender.objects.all())

    def list(self, request, *args, **kwargs):
        response = super(TenderViewSet, self).list(request, *args, **kwargs)
        return Response({'data': response.data, 'request': request, 'title': self.basename.capitalize()},
                        template_name='flags/tenders_list.html')


class LotViewSet(viewsets.ModelViewSet):
    serializer_class = LotSerializer
    permission_classes = (MainAccessPolicy,)
    pagination_class = CustomPagination
    renderer_classes = [TemplateHTMLRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Lot.objects.all())

    def list(self, request, *args, **kwargs):
        response = super(LotViewSet, self).list(request, *args, **kwargs)
        return Response({'data': response.data, 'request': request, 'title': self.basename.capitalize()},
                        template_name='flags/lots_list.html')


class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer
    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Entity.objects.all())

    renderer_classes = [TemplateHTMLRenderer, BrowsableAPIRenderer]

    def list(self, request, *args, **kwargs):
        response = super(EntityViewSet, self).list(request, *args, **kwargs)
        return Response({'data': response.data, 'request': request, 'title': self.basename.capitalize()},
                        template_name='flags/entities_list.html')


class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    permission_classes = (MainAccessPolicy,)
    # renderer_classes = [TemplateHTMLRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Classifier.objects.all())


class BidViewSet(viewsets.ModelViewSet):
    serializer_class = BidSerializer
    permission_classes = (MainAccessPolicy,)
    renderer_classes = [TemplateHTMLRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Bid.objects.all())

    def list(self, request, *args, **kwargs):
        response = super(BidViewSet, self).list(request, *args, **kwargs)
        return Response({'data': response.data, 'request': request, 'title': self.basename.capitalize()},
                        template_name='flags/bids_list.html')


class IrregularityViewSet(viewsets.ModelViewSet):
    serializer_class = IrregularitySerializer
    queryset = Irregularity.objects.all()
    permission_classes = (MainAccessPolicy,)
    renderer_classes = [TemplateHTMLRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Irregularity.objects.all())

    def list(self, request, *args, **kwargs):
        response = super(IrregularityViewSet, self).list(request, *args, **kwargs)
        return Response({'data': response.data, 'request': request, 'title': self.basename.capitalize()},
                        template_name='flags/irregularities_list.html')


class FlagViewSet(viewsets.ModelViewSet):
    serializer_class = FlagSerializer
    renderer_classes = [TemplateHTMLRenderer, BrowsableAPIRenderer]

    filterset_fields = {
        'irregularity': ['exact'],
        'tender': ['exact'],
        'tender__procuring_entity': ['exact'],
        'tender__procuring_entity__name': ['icontains']
    }

    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Flag.objects.all())

    def list(self, request, *args, **kwargs):
        response = super(FlagViewSet, self).list(request, *args, **kwargs)
        return Response({'data': response.data, 'request': request, 'title': self.basename.capitalize()},
                        template_name='flags/flags_list.html')


class FlagDataViewSet(viewsets.ModelViewSet):
    serializer_class = FlagDataSerializer
    permission_classes = (MainAccessPolicy,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Flag.objects.all())

    # renderer_classes = [TemplateHTMLRenderer]
    #
    # def list(self, request, *args, **kwargs):
    #     response = super(FlagDataViewSet, self).list(request, *args, **kwargs)
    #     return Response({'data': response.data, 'request': request, 'title': self.basename.capitalize()},
    #                     template_name='flags/flag_data.html')