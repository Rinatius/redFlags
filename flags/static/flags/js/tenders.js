$(document).ready(function() {
    AjaxDatatableViewUtils.initialize_table(
        $('#datatable_redflags'),
        $("#Url").attr("data-url"),
        {
        // ordering: false,
        // paging: false,
        scrollX: false,
        //language: {
        //        "emptyTable":     "Ой, тут пусто",
        //        "info":           "Строки с _START_ по _END_ из _TOTAL_ объектов",
        //        "infoEmpty":      "Строки с 0 по 0 из 0 объектов",
        //        "infoFiltered":   "(filtered from _MAX_ total entries)",
        //        // "infoPostFix":    "",
        //        // "thousands":      ",",
        //        "lengthMenu":     "_MENU_ Объектов на странице",
        //        "loadingRecords": "Загрузка...",
        //        "processing":     "Обработка...",
        //        "search":         "Поиск:",
        //        "zeroRecords":    "Тут ничего нет",
        //        "paginate": {
        //                "first": "Первая",
        //                "last": "Последняя",
        //                "next": "Следующая",
        //                "previous": "Предыдущая"
        //                }
        //        },

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