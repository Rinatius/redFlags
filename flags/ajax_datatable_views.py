from ajax_datatable.views import AjaxDatatableView
from django.db.models import Count
from django.template.loader import render_to_string

from flags.models import Tender, Flag


def get_param(key, request):
    try:
        value = request.POST.get(key)
    except:
        value = None
    return value


class RedFlagsAjaxDatatableView(AjaxDatatableView):

    model = Tender
    title = 'Tenders'
    initial_order = [['start_time', 'des'], ]

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {
            'name': 'id',
            'visible': False,
            # 'orderable': True,
        },
        {
            'name': 'procuring_entity',
            'searchable': False,
            'orderable': False,
            'max_length': 50,
            'foreign_field': 'procuring_entity__name',
        },
        {
            'name': 'Tender',
            'searchable': False,
            'orderable': False,
         },
        {
            'name': 'Status',
            'searchable': False,
            'orderable': False,
         },
        {
            'name': 'Method',
            'searchable': False,
            'orderable': False,
         },
        {
            'name': 'Price',
            'searchable': False,
            'orderable': False,
         },
        {
            'name': 'start_time',
            'searchable': False,
            'orderable': True,
         },
        {
            'name': 'end_time',
            'searchable': False,
            'orderable': False,
         },
        {
            'name': 'Flags',
            'searchable': False,
            'orderable': True,
            'max_length': 4,
            # 'm2m_foreign_field': 'flags__name',
        },
    ]

    def render_row_details(self, pk, request=None):
        flags = self.model.objects.get(pk=pk).flags.all()
        html = render_to_string('flags/row_details.html', {
            'model': self.model,
            'model_admin': self.get_model_admin(),
            'flags': flags,
        })
        return html

    def customize_row(self, row, obj):
        desc = obj.description.split(' - ')
        # row['Flags'] = len(obj.flags.all()) * '🚩'
        row['Flags'] = len(obj.flags.all())
        row['Status'] = desc[0]
        row['Method'] = desc[1]
        row['Price'] = int(float(desc[2].replace(' KGS', '')))
        row['Tender'] = f'<a href="{obj.url}" target="_blank">{obj.name}</a>'

    def get_initial_queryset(self, request=None):
        flags_id = Flag.objects.all().values_list('tender_id')
        queryset = Tender.objects.filter(pk__in=flags_id)

        flag_type = get_param('flag_type', request)
        if flag_type is not None and flag_type != '':
            queryset = queryset.filter(flags__name=flag_type)

        from_date = get_param('from_date', request)
        if from_date is not None and from_date != '':
            queryset = queryset.filter(start_time__gte=from_date)

        to_date = get_param('to_date', request)
        if to_date is not None and to_date != '':
            queryset = queryset.filter(start_time__lte=to_date)

        procuring_entity = get_param('procuring_entity', request)
        if procuring_entity is not None and procuring_entity != '':
            queryset = queryset.filter(procuring_entity__name__icontains=procuring_entity)

        tenders = get_param('tenders', request)
        if tenders is not None and tenders != '':
            queryset = queryset.filter(name__icontains=tenders)

        return queryset

    def render_clip_value_as_html(self, long_text, short_text, is_clipped):
        return "<span title='{long_text}'>{short_text}{ellipsis}</span>".format(
            long_text=long_text,
            short_text=short_text,
            ellipsis='&hellip;' if is_clipped else ''
        )
