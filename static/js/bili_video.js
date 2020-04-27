$(function () {
    // bili_video
    var width_video_div = $(".clan-video").width();
    $("#bili_video").width(width_video_div * 0.95).height(width_video_div * 0.95 / 16 * 9);
    $(window).resize(function () {
        var width_video_div = $(".clan-video").width();
        $('#bili_video').width(width_video_div * 0.95).height(width_video_div * 0.95 / 16 * 9);
    });



});