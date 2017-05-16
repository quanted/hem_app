/**
 * Created by dlyons on 2/15/2017.
 */


$(function() {
    $('#toggle-event').change(function() {
        $('#console-event').html('Toggle: ' + $(this).prop('checked'))
    })
})
