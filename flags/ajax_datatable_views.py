from ajax_datatable.views import AjaxDatatableView
from flags.models import Tender


class RedFlagsAjaxDatatableView(AjaxDatatableView):

    model = Tender
    title = 'Tenders'
    initial_order = [['start_time', 'asc'], ]

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False},
        {'name': 'name', 'visible': True},
        {'name': 'description', 'visible': True},
        {'name': 'url', 'visible': True},
        # {'name': 'start_time', 'visible': True},
        # {'name': 'end_time', 'visible': True},
        # {'name': 'procuring_entity', 'visible': True},
    ]
