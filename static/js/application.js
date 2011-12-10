$(document).ready(function() {
    $(".dropdown-toggle, .menu, .dropdown-menu").hover(function (e) {
        var $li = $(this).parent("li").toggleClass('open');
        return false;
    });

    $(function() {
        $("#accordion").accordion();
    });

    $(function () {
        $('.tabs').tabs()
    })
});