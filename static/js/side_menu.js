$(function () {
    $(document).scroll(function () {
        var scroH = $(document).scrollTop();  //滚动高度
        // var offset = $(".main-info").offset().top;
        $(".side-menu").css("top",scroH);
    });
    $.get("/api/user/",function(data){
        if(data.msg==="ok"){
            var username = data.user.u_name;
            var avater = data.user.u_avater;
            var email = data.user.u_email;
            var sign = data.user.u_sign;
            var admin = data.user.is_admin;
            $("#side-menu-username").text(username);
            $("#side-menu-email").text(email);
            $("#side-menu-sign").text(sign);
            $("#side-avater").attr("src",avater);
            if(admin === true){
                $(".uib-admin button").css("display","inline")
            }
        }else{
            console.log("no login")
        }
    });


});