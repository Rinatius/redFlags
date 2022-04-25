from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from flags.models import Entity, Tender, Lot, Classifier, Bid, Irregularity, Flag
from flags.permissions import MainAccessPolicy
from flags.serializer import TenderSerializer, LotSerializer, EntitySerializer, ClassifierSerializer, BidSerializer, \
    IrregularitySerializer, FlagSerializer, FlagDataSerializer

from .filters import TenderFilter


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class FlagDetailsView(DetailView):
    model = Flag
    template_name = 'flags/flag_details.html'


class MainPageView(ListView):
    template_name = 'flags/django_front.html'
    paginate_by = 20
    # paginator_class = CustomPagination

    def get_queryset(self):
        flags_id = Flag.objects.all().values_list('tender_id')
        tenders = Tender.objects.filter(pk__in=flags_id)
        filter1 = TenderFilter(self.request.GET, tenders)
        return filter1.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter1 = TenderFilter(self.request.GET, queryset)
        context["filter"] = filter1
        return context

# class MainPageView(viewsets.ModelViewSet):
#     serializer_class = TenderSerializer
#     permission_classes = (MainAccessPolicy,)
#     renderer_classes = [TemplateHTMLRenderer]
#     # pagination_class = CustomPagination
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = CustomFilter
#
#     def get_queryset(self):
#         flags_id = Flag.objects.all().values_list('tender_id')
#         tenders = Tender.objects.filter(pk__in=flags_id)
#
#         return MainAccessPolicy.scope_queryset(self.request, tenders.order_by('-start_time'))
#
#     def list(self, request, *args, **kwargs):
#         response = super(MainPageView, self).list(request, *args, **kwargs)
#         return Response({
#             'data': response.data,
#             'filter': CustomFilter,
#         }, template_name='flags/main_front.html')


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
