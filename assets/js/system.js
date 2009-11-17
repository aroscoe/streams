/* SYSTEM **************************************************/

$(document).ready(function(){
    $("#add_stream a").click(function(e){
        e.preventDefault();
        if ($(this).attr("class") == "active") {
            console.log("hey!");
        } else {
            $(this).addClass("active");
            $(this).find("em").hide();
            $(this).parent().find("input").show();
        }
    });

    $("#layout_changer").click(function(){
        wrapper = $("div.layout_wrapper");
        if (wrapper.attr("class") == "") {
            wrapper.addClass("inactive");
        } else {
            wrapper.removeClass("inactive");
        }
    });
});