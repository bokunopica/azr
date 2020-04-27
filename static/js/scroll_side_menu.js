$(function () {
    $(document).scroll(function () {
        var scroH = $(document).scrollTop();  //滚动高度
        var offset = $(".main-info").offset().top;
        $(".side-menu").css("top",scroH);
    });
});