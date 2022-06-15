$(document).ready(function() {
    AjaxDatatableViewUtils.initialize_table(
        $('#datatable_redflags'),
        $("#Url").attr("data-url"),
        {
        // ordering: false,
        scrollX: false,
        dom: "<'row justify-content-between'<'col-auto'l><'col-auto'B>>rt<'row justify-content-between'<'col-auto'i><'col-auto'p>>",
        buttons: {
            dom: {
                button: {
                    className: 'btn btn-sm btn-primary buttons-html5'
                }
            },
            buttons: [

            {
            extend: 'copy',
            text: 'Скопировать',
            className: 'buttons-copy'
        },
        {
            extend: 'csv',
            text: 'Сохранить в csv',
            className: 'buttons-csv',
//            customize: function(csv) {
//                return csv
//            }
        }
        ],
        },
        language: {
                "emptyTable":     "Ой, тут пусто",
                "info":           "Строки с _START_ по _END_ из _TOTAL_ объектов",
                "infoEmpty":      "Строки с 0 по 0 из 0 объектов",
                "infoFiltered":   "(filtered from _MAX_ total entries)",
                // "infoPostFix":    "",
                // "thousands":      ",",
                "lengthMenu":     "_MENU_ Объектов на странице",
                "loadingRecords": "Загрузка...",
                "processing":     "Загрузка...",
                "search":         "Поиск:",
                "zeroRecords":    "Тут ничего нет",
                "paginate": {
                        "first": "Первая",
                        "last": "Последняя",
                        "next": "Следующая",
                        "previous": "Предыдущая"
                        }
                },

        },
        {
            flag_type: function() { return $('input#flag_type').val() },
            from_date: function() { return $('input#from_date').val() },
            to_date: function() { return $('input#to_date').val() },
            tenders: function() { return $('input#tenders').val() },
            procuring_entity: function() { return $('input#procuring_entity').val() },
        }
    );

    $('#from_date').dtDateTime();
    $('#to_date').dtDateTime();
    $('.filters').on('change paste', function() {
    $('#datatable_redflags').DataTable().ajax.reload(null, false);
});
});