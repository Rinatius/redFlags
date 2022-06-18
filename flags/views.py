from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from flags.models import Entity, Tender, Lot, Classifier, Bid, Irregularity, Flag
from flags.permissions import MainAccessPolicy
from flags.serializer import TenderSerializer, LotSerializer, EntitySerializer, ClassifierSerializer, BidSerializer, \
    IrregularitySerializer, FlagSerializer

from django.shortcuts import render


def table(request):
    return render(request, 'flags/tenders.html', {})


def home_page(request):
    return render(request, 'flags/home_page.html')


class FlagDetailsView(DetailView):
    model = Flag
    template_name = 'flags/flag_details.html'


class TenderViewSet(viewsets.ModelViewSet):
    serializer_class = TenderSerializer
    permission_classes = (MainAccessPolicy,)

    def get_queryset(self):
        return MainAccessPolicy.scope_queryset(self.request, Tender.objects.all())


class LotViewSet(viewsets.ModelViewSet):
    serializer_class = LotSerializer
    permission_classes = (MainAccessPolicy,)

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

