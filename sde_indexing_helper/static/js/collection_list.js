let table = $('#collection_table').DataTable({
    paging: false,
    dom: 'iftip',
    order: [[5, 'asc']],
    columnDefs: [
        {
            target: -1,
            visible: false,
        },
        {
            target: 2,
            sortable: false,
        },
    ],
    initComplete: function () {
        this.api().columns(2).every(function () {
            var column = this;
            var select = $('<select><option value=""></option></select>')
                .appendTo($(column.header()))
                .on('change', function () {
                    var val = $.fn.dataTable.util.escapeRegex(
                        $(this).val()
                    );

                    column
                        .search(val ? '^' + val + '$' : '', true, false)
                        .draw();
                });

            column.data().unique().sort().each(function (d, j) {
                select.append('<option value="' + d + '">' + d + '</option>')
            });
        });
        this.api().columns(7).every(function () {
            var column = this;
            var select = $('<select><option value=""></option></select>')
                .appendTo($(column.header()))
                .on('change', function () {
                    var val = $.fn.dataTable.util.escapeRegex(
                        $(this).val()
                    );

                    column
                        .search(val ? '^' + val + '$' : '', true, false)
                        .draw();
                });

            column.data().unique().sort().each(function (d, j) {
                select.append('<option value="' + d + '">' + d + '</option>')
            });
        });
    }
});

var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();

function handleDocumentTypeSelect() {
    $("body").on("click", ".curation_status_select", function () {
        var collection_id = $(this).data('collection-id');
        var curation_status = $(this).attr('value');
        postCurationStatus(collection_id, curation_status);
    });
}

function postCurationStatus(collection_id, curation_status) {
    var url = `/api/collections/${collection_id}/`;
    $.ajax({
        url: url,
        type: "PUT",
        data: {
            curation_status: curation_status,
            csrfmiddlewaretoken: csrftoken
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function (data) {
            location.reload();
        },
    });
}

$(document).ready(function () {
    setupClickHandlers();
});

function setupClickHandlers() {
    handleDocumentTypeSelect();
}
