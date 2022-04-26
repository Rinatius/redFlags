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
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'list': 'entitiesList',
            'placeholder': 'Name of procuring entity',
            'id': 'inputProcuringEntity',
        }),
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

    flag_name = django_filters.CharFilter(
        field_name='flag__name',
        distinct=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'list': 'flagsList',
            'id': 'inputFlagType',
        }),
    )

    # flag_created_at = django_filters.DateFilter(
    #     field_name='flag__created_at',
    #     distinct=True,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'data-provide': 'datepicker',
    #         'data-date-format': 'mm/dd/yyyy',
    #     })
    # )

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputTenderName',
        }),
    )

    class Meta:
        model = Tender
        fields = [
            'procuring_entity',
            # 'flag',
        ]
