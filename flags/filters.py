from django.forms import CharField
from django.template import loader
from django_filters.fields import ModelChoiceField
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django import forms
from .models import Tender


class NoMarkupDjangoFilterBackend(DjangoFilterBackend):
    def to_html(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        if filterset is None:
            return None

        for key, value in filterset.form.fields.items():
            if isinstance(value, ModelChoiceField):
                filterset.form.fields[key] = CharField(label=value.label, disabled=value.disabled,
                                                       help_text=value.help_text, required=value.required)

        template = loader.get_template(self.template)
        context = {'filter': filterset}
        return template.render(context, request)


class TenderFilter(django_filters.FilterSet):

    procuring_entity = django_filters.CharFilter(
        field_name='procuring_entity__name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'list': 'entitiesList',
            'placeholder': 'Название закупающей организации',
            'id': 'inputProcuringEntity',
        }), label='',
    )

    start_date_from = django_filters.DateFilter(
        field_name='start_time',
        lookup_expr='gte',
        label='Дата начала тендера больше или равна',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            # 'style': 'width: 300px;',
            'data-date-format': 'mm/dd/yyyy',
            'placeholder': 'From',
        })
    )

    start_date_to = django_filters.DateFilter(
        field_name='start_time',
        lookup_expr='lte',
        label='Дата начала тендера меньше или равна',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            # 'style': 'width: 300px;',
            'data-date-format': 'mm/dd/yyyy',
            'placeholder': 'To',
        })
    )

    end_date_from = django_filters.DateFilter(
        field_name='end_time',
        lookup_expr='gte',
        label='Дата конца тендера больше или равна',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            # 'style': 'width: 300px;',
            'data-date-format': 'mm/dd/yyyy',
            'placeholder': 'From',
        })
    )

    end_date_to = django_filters.DateFilter(
        field_name='end_time',
        lookup_expr='lte',
        label='Дата конца тендера меньше или равна',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-provide': 'datepicker',
            # 'style': 'width: 300px;',
            'data-date-format': 'mm/dd/yyyy',
            'placeholder': 'To',
        })
    )

    class Meta:
        model = Tender
        fields = [
            'procuring_entity',
        ]
