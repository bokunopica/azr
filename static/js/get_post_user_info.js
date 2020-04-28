$(function () {
    var url = "/api/user/";
    $.get(url, function (data, statusText, xhr) {
        /**
         * 用户信息界面信息填充
         */
        if (data.msg === "ok") {
            var username = data.user.u_name;
            var u_sign = data.user.u_sign;
            var u_email = data.user.u_email;
            var avater = $("#avater img").attr("src");
            $(".username-api-info").text(username);
            $(".email-api-info").text(u_email);
            $(".avater-api-info").attr("src", avater);
            $(".sign-api-info").text(u_sign);
        } else {
            console.log("no login")
        }
    });
    var email_send_button = $("#email-send-button");
    email_send_button.click(
        /**
         * 发送邮件验证
         * 1.判断按钮状态,可点击则继续,不可点击就不反应
         * 2.发送数据至api接口,按钮变为不可点击状态
         * 3.设置定时器修改按钮不可点击时间,当不可点击时间<=0时按钮变回原来状态
         */
        function () {
            email_send_button.attr("disabled", true);
            var send_wait_time = 5;
            email_send_button.text(send_wait_time + "s");
            time_change = setInterval(function () {
                if (send_wait_time <= 1) {
                    email_send_button.attr("disabled", false);
                    email_send_button.text("发送验证码");
                    clearInterval(time_change);
                } else {
                    send_wait_time -= 1;
                    email_send_button.text(send_wait_time + "s");
                }
            }, 1000);

            var email_send_api = "/api/user/mail_check/";
            var email_send_text = $("#email-send-text");
            $.post(email_send_api, function (data, statusText, xhr) {
                /**
                 * 用户信息界面信息填充
                 */
                if (data.msg === "ok") {
                    email_send_text.text("已发送");
                    email_send_text.css("color", "white");
                } else if (data.msg === "activated") {
                    email_send_text.text("您已激活邮箱!请勿再试");
                    email_send_text.css("color", "yellow");
                } else {
                    email_send_text.text("发送失败");
                    email_send_text.css("color", "red");
                }
            });
        });

    var email_check_button = $("#email-check-button");
    email_check_button.click(
        /**
         * 邮件确认
         * 1.发送验证码数据至接口,判定是否正确
         * 2.正确则验证通过,显示验证通过字样
         * 3.失败则显示验证失败字样
         */
        function () {
            var email_verify_code_input = $("#email-check-verify-code");
            var verify_code = email_verify_code_input.val();
            var email_check_text = $("#email-check-text");
            if (verify_code.length === 4) {
                verify_code = verify_code.toLowerCase();
                var email_check_url = "/api/user/mail_check/?verify_code=" + verify_code;

                $.ajax({
                    url: email_check_url,
                    type: 'PUT',
                    success: function (data, statusText, xhr) {
                        /**
                         * 验证邮箱验证码
                         */
                        if (data.msg === "ok") {
                            email_check_text.text("邮箱验证成功")
                            email_check_text.css("color", "white");
                        } else if (data.msg === "activated") {
                            email_check_text.text("您已激活邮箱!请勿再试");
                            email_check_text.css("color", "yellow");
                        } else {
                            email_check_text.text("验证失败");
                            email_check_text.css("color", "red");
                        }
                    }
                })
            } else {
                email_check_text.text("请输入正确的验证码");
            }
        }
    );

    var sign_change_button = $("#sign-change-button");
    sign_change_button.click(function () {
        var sign_change_input = $("#sign-change-input").val();
        var sign_change_text = $("#sign-change-text");
        if (sign_change_input.length === 0) {
            sign_change_text.text("请输入正确的文本");
            sign_change_text.css("color", "yellow");
        } else if (sign_change_input.length > 25) {
            sign_change_text.text("文本过长,超过25个字符");
            sign_change_text.css("color", "red");
        } else {
            $.ajax({
                url: "/api/user/sign_change/?sign=" + sign_change_input,
                type: 'PUT',
                success: function (data, statusText, xhr) {
                    /**
                     * 修改签名
                     */
                    if (data.msg === "ok") {
                        sign_change_text.text("修改成功");
                        sign_change_text.css("color", "white");
                        $("#sign-now").text(sign_change_input);
                    } else {
                        sign_change_text.text("修改失败");
                        sign_change_text.css("color", "yellow");
                    }
                }
            })
        }
    });

    $("#sign-change-input").on("input propertychange", function () {
        /**
         * 字数输入限制
         */
        var $this = $(this),
            _val = $this.val();
        if (_val.length > 25) {
            $this.val(_val.substring(0, 25));
        }
    });


    var avater_change_button = $("#avater-change-button");


    $("#avater_upload").change(function () {
        var file = $("#avater_upload").get(0).files[0];
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function () {
            $("#avater_upload_show").attr("src", reader.result);
        };

    });


    avater_change_button.click(function () {
        var IMG_BASE = $("#avater_upload_show").attr("src"); //要上传的图片的base64编码
        var IMG_ROUTE = $("#avater_upload").val();//获取上传图片路径，为获取图片类型使用
        var IMG_ENDFOUR = IMG_ROUTE.substr(IMG_ROUTE.length - 4, 4);//截取路径后四位，判断图片类型
        var IMG_FORMAT = "jpeg"; //图片类型***
        if (IMG_ENDFOUR.trim() === ".jpg")
            IMG_FORMAT = "jpg";
        else if (IMG_ENDFOUR.trim() === ".png")
            IMG_FORMAT = "png";
        else if (IMG_ENDFOUR.trim() === ".bmp")
            IMG_FORMAT = "bmp";
        //图片正式开始上传
        $.ajax({
            type: "PUT",
            url: "/api/user/avater_change/",
            data: JSON.stringify(
                {'imgBase': IMG_BASE, 'imgFormat': IMG_FORMAT},
            ),
            dataType: "json",
            success: function (data) {
                alert(data.msg);
            }
        });
    });

    $("#password-change-button").click(function () {
        var new_password = $("#new-password-input").val();
        var old_password = $("#old-password-input").val();
        if (new_password === $("#new-password-input-confirm").val() && new_password !== old_password) {
            $.ajax({
                type: "put",
                url: "/api/user/pwd_change/",
                data: JSON.stringify({'oldpwd': old_password, 'newpwd': new_password}),
                dataType: "json",
                contentType:"application/json",
                success: function (data) {
                    if (data.msg === "ok") {
                        $("#password-change-text").text("修改密码成功");
                    }
                }
            });
            $("#password-change-text").text("修改密码失败");
        } else {
            $("#password-change-text").text("修改密码失败");
        }
    });

    $("#new-password-input").blur(function () {
        if ($("#new-password-input").val() === $("#old-password-input").val()) {
            $("#new-password-input-text").text("请不要使用跟旧密码相同的密码").css("color", "red");
        }else{
            $("#new-password-input-text").text("");
        }
    });

    $("#new-password-input-confirm").blur(function () {
        if ($("#new-password-input").val() !== $("#new-password-input-confirm").val()) {
            $("#new-password-input-confirm-text").text("两次新密码输入不同").css("color", "red");
        }else{
            $("#new-password-input-confirm-text").text("")
        }
    });
});