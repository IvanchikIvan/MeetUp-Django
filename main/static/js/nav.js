"use strict";

let menu_open = false


$("#menu").click(() => {
    if (menu_open) { // действия при закрытии меню
        $('#nav').addClass("nav-no_open")
        $('#nav').removeClass("nav-open")   
        $('.title').addClass("close")
        $('.meets').addClass("close")

        $('#meets_icon').removeClass("meets_icon-open")
        $('#meets__nav').addClass("meets__nav-close")
        $('#meets__nav').removeClass("meets__nav-open")

        menu_open = false    
    }
    else { // действия при открытии меню
        $('#nav').addClass("nav-open")    
        $('#nav').removeClass("nav-no_open")
        $('.title').removeClass("close")
        $('.meets').removeClass("close")
        menu_open = true    
    }
});


$("#meets_icon").click(() => {
    $('#meets_icon').toggleClass("meets_icon-open")
    $('#meets__nav').toggleClass("meets__nav-close")
    $('#meets__nav').toggleClass("meets__nav-open")
});
