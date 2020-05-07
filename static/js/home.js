$(function () {
    // bili_video
    var width_video_div = $(".clan-video").width();
    $("#bili_video").width(width_video_div * 0.95).height(width_video_div * 0.95 / 16 * 9);
    $(window).resize(function () {
        var width_video_div = $(".clan-video").width();
        $('#bili_video').width(width_video_div * 0.95).height(width_video_div * 0.95 / 16 * 9);
    });

    $.ajax({
        type: "GET",
        url: "/api/user/cm/",
        dataType: "json",
        success: function (data) {
            $(".clan-user-one").remove();

            for(var i =0;i<data.users.length;i++){
                var user = data.users[i];
                var element = "<div class='clan-user-one'><img src="+user.u_avater+" alt=''><p>"+user.u_name+"</p></div>";
                $(element).appendTo($(".clan-user"))
            }
            $(".clan-user-one img").width("80%").height("80%");
        }
    });


});