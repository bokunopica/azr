$(function(){
    var loginButton = $("#login-button");
    loginButton.click(function(){
        $.post("/api/user/login_register/?action=login",{
        username:$("#login-input-username input").val(),
        password:$("#login-input-password input").val(),
        },function(data,statusText,xhr){
            if(data.msg==="login success"){
                alert("登录成功");
                $.cookie("access_token",data.access_token,{expires:1,path: '/'});
                window.location.href = "http://" + window.location.host + "/home/";
            }else{
                alert("登录失败");
            }
        });
    });
});