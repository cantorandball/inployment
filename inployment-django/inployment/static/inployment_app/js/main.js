$( document).ready(function() {
    $(".email-box").bind({
        /*
        mouseenter: function () {
            $(this).children(".blinds").show("blind");
        },
        mouseleave: function () {
            $(this).children(".blinds").hide("blind");
        }
         */

        click: function () {
            $(this).children(".blinds").toggle("blind");
        }
    });

    // Stop the div from closing when an input element is clicked
    $(".form-control").click(function(e){
        e.stopPropagation();
    });
});