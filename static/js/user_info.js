$(function(){
    var url = "/api/user/";
    $.get(url,function(data,statusText,xhr){
        if(data.msg==="ok"){
            var username = data.user.u_name;
            var u_avater = data.user.u_avater;
            var img_html = "<img src="+u_avater+">";
            var username_html = "<a href="+"/userinfo/"+">"+"";
            $("#avater").html(img_html);
            $("#top-nav-bar-right-1 div").html(username_html);
            $("#top-nav-bar-right-1 div a").text(username);
        }else{
            console.log("no login")
        }
    });
});