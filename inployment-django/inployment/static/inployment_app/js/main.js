$( document).ready(function() {

    $(".email-box").click(function () {
        $(this).children(".blinds").toggle("blind", {"direction": "down"});
    });

});