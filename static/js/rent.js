$(function () {
    $("#save-rent-info").click(function () {
        $('#myModal').modal('hide');
    });

    $("#year-toggle li a").click(function(){
        var year_select = this.text;
        $("#year-selected").text(year_select);
    });
    $("#month-toggle li a").click(function(){
        /*
        *
        * */
        var month_select = this.text;
        $("#month-selected").text(month_select);
    })

});