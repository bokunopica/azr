$(function(){
    var url = "/api/user/";
    $.get(url,function(data,statusText,xhr){
        if(data.msg==="ok"){
            var username = data.user.u_name;
            var u_sign = data.user.u_sign;
            var u_email = data.user.u_email;
            var avater = $("#avater img").attr("src");
            $(".username-api-info").text(username);
            $(".email-api-info").text(u_email);
            $(".avater-api-info").attr("src",avater);
            $(".sign-api-info").text(u_sign);
        }else{
            console.log("no login")
        }
    });
});