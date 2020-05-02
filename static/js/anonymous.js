$(function () {
    $.ajax({
        type: "GET",
        url: "/api/user/amsg/",
        dataType: "json",
        success: function (data) {
            if(data.msg === "ok"){
                var anonymous_titles = data.anonymous;
                for(var i =0;i<data.anonymous.length-1;i++){
                    $("#anonymous-info-wrap").clone().appendTo($(".anonymous-info"));
                }
                for(var j=0;j<anonymous_titles.length;j++){
                    $(".an_titles").eq(j).attr("href","/anonymous/"+anonymous_titles[j].id+"/").text(anonymous_titles[j].a_content);
                    var unixTimestamp = new Date(anonymous_titles[j].a_timestamp * 1000);
                    var commonTime = unixTimestamp.toLocaleString();
                    $(".message-time").eq(j).text(commonTime);
                    $(".message-button button").eq(j).attr("name",anonymous_titles[j].id).click(function(){
                        var a_id = $(this).attr("name");
                        // 删除帖子
                        $.ajax({
                            type:"DELETE",
                            url:"/api/admin/an/",
                            data:{"a_id":a_id},
                            dataType:"json",
                            success:function(data){
                                location.reload();
                            }
                        })
                    });
                }
            }
        }
    });

    $.ajax({
        type:"GET",
        url:"/api/user/",
        dataType:"json",
        success:function(data){
            if(data.user.is_admin){
                $(".message-button").css("display","inline");
            }
        }
    });


    $("#publish-confirm").click(
        function(){
            var a_title = $("#anonymous-title").val();
            var a_content = $("#anonymous-msg") .val();
            var warn = $("#publish-warn");
            if(a_title.length>0 && a_content.length>0){
                warn.css("display","none");
                $.ajax({
                    type: "POST",
                    url: "/api/user/amsg/",
                    data:{"a_title":a_title,"a_content":a_content},
                    dataType: "json",
                    success: function (data) {
                        if(data.msg === "created success"){
                            warn.css("display","inline").css("color","white").text("成功");
                            location.reload();
                        }else{
                            warn.css("display","inline").css("color","red").text("发帖失败,请您重试");
                        }

                    }
                });
            }else{
                warn.css("display","inline").css("color","red").text("请输入正确的标题和内容");
            }
        }
    )


});