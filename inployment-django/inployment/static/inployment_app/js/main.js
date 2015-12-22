$( document).ready(function() {

    $(".email-box").click(function () {
        $(this).children(".colour-container").toggle("blind", {"direction": "down"});
    });

});