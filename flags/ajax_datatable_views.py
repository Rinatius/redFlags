from ajax_datatable.views import AjaxDatatableView
from django.template.loader import render_to_string

from flags.models import Tender, Flag


class RedFlagsAjaxDatatableView(AjaxDatatableView):

    model = Tender
    title = 'Tenders'
    initial_order = [['name', 'asc'], ]
    latest_by = 'start_time'

    def render_row_details(self, pk, request=None):
        flags = self.model.objects.get(pk=pk).flags.all()
        html = render_to_string('flags/row_details.html', {
            'model': self.model,
            'model_admin': self.get_model_admin(),
            'flags': flags,
        })
        return html

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False},
        {'name': 'procuring_entity', 'max_length': 40, 'foreign_field': 'procuring_entity__name'},
        {'name': 'name', 'title': 'Tender', 'max_length': 20},
        {'name': 'Status'},
        {'name': 'Method'},
        {'name': 'Price'},
        # {'name': 'description', 'max_length': 40},
        # {'name': 'url'},
        {'name': 'start_time', 'max_length': 10},
        {'name': 'end_time', 'max_length': 10},
        {'name': 'Flags'},
    ]

    def customize_row(self, row, obj):
        row['Flags'] = len(obj.flags.all()) * '🚩'

        desc = obj.description.split(' - ')
        row['Status'] = desc[0]
        row['Method'] = desc[1]
        row['Price'] = int(float(desc[2].replace(' KGS', '')))

    def get_initial_queryset(self, request=None):
        flags_id = Flag.objects.all().values_list('tender_id')
        tenders = Tender.objects.filter(pk__in=flags_id)
        return tenders

    def render_clip_value_as_html(self, long_text, short_text, is_clipped):
        return "<span title='{long_text}'>{short_text}{ellipsis}</span>".format(
            long_text=long_text,
            short_text=short_text,
            ellipsis='&hellip;' if is_clipped else ''
        )