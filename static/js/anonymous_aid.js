$(function () {
    var location_split = location.href.split("/");
    var a_id = location_split[location_split.length-2];
    $.ajax({
        type: "GET",
        url: "/api/user/amsg/"+a_id+"/",
        dataType: "json",
        success: function (data) {
            if(data.msg === "query ok"){
                $("#a-title").text(data.anonymous.a_title);
                $(".a_content").text(data.anonymous.a_content);
                var unixTimestamp = new Date(data.anonymous.a_timestamp * 1000);
                var commonTime = unixTimestamp.toLocaleString();
                $(".message-time").text(commonTime);
                var replies = data.replies;
                for(var i =0;i<replies.length;i++){
                    $("#anonymous-info-wrap").clone().appendTo($(".anonymous-info"));
                }
                for(var j=0;j<replies.length;j++){
                    $(".a_content").eq(j+1).text(replies[j].am_content);
                    var unixTimestamp = new Date(replies[j].am_timestamp * 1000);
                    var commonTime = unixTimestamp.toLocaleString();
                    $(".message-time").eq(j+1).text(commonTime);
                    $(".message-floor").eq(j+1).text(replies[j].am_floor+"楼");
                    $(".message-button").eq(j+1).attr("name",replies[j].id).click(function(){
                        var am_id = $(this).attr("name");
                        $.ajax({
                            type:"DELETE",
                            url:"/api/admin/am/",
                            data:{"am_id":am_id},
                            dataType:"json",
                            success:function(){
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
                $(".message-button").css("display","inline").eq(0).css("display","none");
            }
        }
    });

    $("#publish-confirm").click(
        function(){
            var am_content = $("#anonymous-msg").val();
            var warn = $("#publish-warn");
            if(am_content.length>0){
                warn.css("display","none");
                $.ajax({
                    type: "POST",
                    url: "/api/user/amsg/"+a_id+"/",
                    data:{"am_content":am_content},
                    dataType: "json",
                    success: function (data) {
                        if(data.msg === "replied success"){
                            warn.css("display","inline").css("color","white").text("成功");
                            location.reload();
                        }
                    }
                });
            }else{
                warn.css("display","inline").css("color","red").text("请输入正确的内容");
            }
        }
    )


});