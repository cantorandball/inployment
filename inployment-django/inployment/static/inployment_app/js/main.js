$( document).ready(function() {
    $(".email-box").bind({
        click: function () {
            $(this).children(".blinds").toggle("blind");
        }
    });

    // Leave blinds closed if errors are present
    $(".blinds").each(function(){
        if($(this).find("ul.errorlist").length){
            $(this).show();
        }
    });

    // Stop the div from closing when an input element is clicked
    $(".form-control, button").click(function(e){
        e.stopPropagation();
    });
});