$(function(){
    var regButton = $("#login-button");
    regButton.click(function(){
        $.post("/api/user/login_register/?action=register",{
        username:$("#login-input-username input").val(),
        password:$.md5($("#login-input-password input").val()),
        email:$("#login-input-email input").val()
        },function(data){
            if(data.msg==="register success"){
                alert("注册成功");
                window.location.href = "http://" + window.location.host + "/login/";
            }else if(data.msg==="email failed"){
                alert("邮箱格式出错");
            }
        });
    });
});