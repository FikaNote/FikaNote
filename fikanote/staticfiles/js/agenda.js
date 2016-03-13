'use strict';

function deleteAgenda() {
    if (!window.confirm("Agendaを削除しますか？")) {
        return;
    }
    //use original 'this'
    $.ajax({
        type: 'DELETE',
        url: '/agenda/',
        dataType:'json',
        data: { id: $(this).attr('id') },
        success: function(res) {
            console.log(res);
        }
    });
    $(this).parent().remove();
}

$(document).ready(function() {
    $(".livepreview").livePreview();
    $('#id_url').focus();
    $('#agenda').submit(function() {  // AJAX by submit
        if ($('#id_url').val() === '') {
            return false;
        }

        var url = $('form#agenda').attr('action');
        var data = {url: $('#id_url').val()};
        var spinner = new Spinner( {
          lines: 11, // The number of lines to draw
          length: 28, // The length of each line
          width: 14, // The line thickness
          radius: 42, // The radius of the inner circle
          scale: 0.25, // Scales overall size of the spinner
          corners: 1, // Corner roundness (0..1)
          color: '#000', // #rgb or #rrggbb or array of colors
          opacity: 0.25, // Opacity of the lines
          rotate: 0, // The rotation offset
          direction: 1, // 1: clockwise, -1: counterclockwise
          speed: 1, // Rounds per second
          trail: 60, // Afterglow percentage
          fps: 20, // Frames per second when using setTimeout() as a fallback for CSS
          zIndex: 2e9, // The z-index (defaults to 2000000000)
          className: 'spinner', // The CSS class to assign to the spinner
          top: '50%', // Top position relative to parent
          left: '50%', // Left position relative to parent
          shadow: false, // Whether to render a shadow
          hwaccel: false, // Whether to use hardware acceleration
          position: 'absolute' // Element positioning
        });
        spinner.spin(document.body);
        $.post(url, data, 'json')
         .done(function(response) {
             $('#agenda_list').prepend('<li><a href="' + response.url + '" target="_blank" class="livepreview"> ' + response.title + '</a><i class="delete-agenda icon-trash-empty" id="' + response.id + '"><span>delete</span></i></li>');
             $('#' + response.id).click(deleteAgenda);
             $('#id_url').val('');
             spinner.spin();
             $('#submit-agenda').prop('disabled', false);
         })
         .fail(function(response) {
             console.warn(response);
             spinner.spin();
             $('#submit-agenda').prop('disabled', false);
         });
         $('#submit-agenda').prop('disabled', true);
        return false;
    });
    $('.delete-agenda').click(deleteAgenda);
});
