from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework_bulk import BulkModelViewSet
from rest_framework.views import APIView
from rest_framework import generics

from flags.models import Entity, Tender, Lot, Classifier, Bid, Irregularity, Flag
from flags.permissions import MainAccessPolicy
from flags.serializer import TenderSerializer, LotSerializer, EntitySerializer, ClassifierSerializer, BidSerializer, \
    IrregularitySerializer, FlagSerializer, FlagDataSerializer

from django_filters import rest_framework as filters
from django import forms


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CustomFilter(filters.FilterSet):
    procuring_entity = filters.CharFilter(
        field_name='procuring_entity__name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'list': 'entitiesList',
            'placeholder': 'Название закупающей организации',
        }), label='',
    )
    # name = filters.ModelChoiceFilter(
    #     field_name='name',
    #     queryset=Irregularity.objects.all(),
    #     label=''
    # )

    start_start_date = filters.DateTimeFilter(
        field_name='start_time',
        lookup_expr='gte',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            'style': 'width: 300px;',
            'data-date-format': 'yyyy-mm-ddT09:12:06.894000Z',
        })
    )
    start_end_date = filters.DateTimeFilter(
        field_name='start_time',
        lookup_expr='lte',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            'style': 'width: 300px;',
            'data-date-format': 'yyyy-mm-ddT00:00:00.000000Z',
        })
    )

    end_start_date = filters.DateTimeFilter(
        field_name='end_time',
        lookup_expr='gte',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            'style': 'width: 300px;',
            'data-date-format': 'yyyy-mm-ddT00:00:00.000000Z',
        })
    )
    end_end_date = filters.DateTimeFilter(
        field_name='end_time',
        lookup_expr='lte',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            'style': 'width: 300px;',
            'data-date-format': 'yyyy-mm-ddT00:00:00.000000Z',
        })
    )

    class Meta:
        model = Tender
        fields = [
            'start_start_date',
            'start_end_date',
            'procuring_entity',
            # 'name',
        ]


class MainPageView(viewsets.ModelViewSet):
    serializer_class = TenderSerializer
    permission_classes = (MainAccessPolicy,)
    renderer_classes = [TemplateHTMLRenderer]
    # pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomFilter

    def get_queryset(self):
        flags_id = Flag.objects.all().values_list('tender_id')
        tenders = Tender.objects.filter(pk__in=flags_id)

        return MainAccessPolicy.scope_queryset(self.request, tenders.order_by('-start_time'))

    def list(self, request, *args, **kwargs):
        response = super(MainPageView, self).list(request, *args, **kwargs)
        return Response({
            'data': response.data,
            'filter': CustomFilter,
        }, template_name='flags/main_front.html')


class TenderViewSet(viewsets.ModelViewSet):
    serializer_class = TenderSerializer
    permission_classes = (MainAccessPolicy,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Tender.objects.all())


class LotViewSet(viewsets.ModelViewSet):
    serializer_class = LotSerializer
    permission_classes = (MainAccessPolicy,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Lot.objects.all())


class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer
    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Entity.objects.all())


class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Classifier.objects.all())


class BidViewSet(viewsets.ModelViewSet):
    serializer_class = BidSerializer
    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Bid.objects.all())


class IrregularityViewSet(viewsets.ModelViewSet):
    serializer_class = IrregularitySerializer
    queryset = Irregularity.objects.all()
    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Irregularity.objects.all())


class FlagViewSet(viewsets.ModelViewSet):
    serializer_class = FlagSerializer

    filterset_fields = {
        'irregularity': ['exact'],
        'tender': ['exact'],
        'tender__procuring_entity': ['exact'],
        'tender__procuring_entity__name': ['icontains']
    }

    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Flag.objects.all())


class FlagDataViewSet(viewsets.ModelViewSet):
    serializer_class = FlagDataSerializer
    permission_classes = (MainAccessPolicy,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Flag.objects.all())
