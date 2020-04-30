$(function(){
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
    $.get("/api/user/users",function(data){
        if(data.msg==="ok"){
            var users = data.users;
            var nums = users.length;
            var user_info_body = $(".user-info-body");
            var user_info_wrap = $("#user-info-wrap");
            for(var i=0;i<nums-1;i++){
                user_info_body.clone().appendTo(user_info_wrap);
            }
            for(var k=0;k<nums;k++){
                var username = users[k].u_name;
                var avater = users[k].u_avater;
                var sign = users[k].u_sign;
                var u_id = users[k].id;
                $(".uib-avater img").eq(k).attr("src",avater);
                $(".uib-name p").eq(k).text(username);
                $(".uib-sign p").eq(k).text(sign);
                $(".uib-admin").eq(k).attr("name","uid:"+u_id);
            }
        }else{
            for(var j=0;j<2;j++){
                $(".user-info-body").clone().appendTo($("#user-info-wrap"));
            }
        }
    });
    $("#user-info-wrap").on("click","#delete-user",function(){
        var _this = $(this);
        var name_id = _this.parent().attr("name");
        var u_id = name_id.split(":")[1];
        $.ajax({
            type: "DELETE",
            url: "/api/admin/user/"+u_id+"/",
            dataType: "json",
            success: function (data) {
                if(data.msg === "delete success"){
                    alert(data.msg);
                    _this.parent().parent().remove();
                }
            }
        });
    }).on("click","#upgrade-clan-user",function(){
        var name_id = $(this).parent().attr("name");
        var u_id = name_id.split(":")[1];
        $.ajax({
            type: "PUT",
            url: "/api/admin/user/"+u_id+"/?action=1",
            dataType: "json",
            success: function (data) {
                if(data.msg === "changed ok"){
                    alert(data.msg);
                }
            }
        });
    });

});