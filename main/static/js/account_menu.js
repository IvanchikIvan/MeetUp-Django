"use strict";

let is_menu_open = false

$("#account").click(() => {
    if (is_menu_open) {
        $('#account__menu').css({'opacity': 0, 'display': 'none'})
        $('#account__menu').removeClass('visible')
        is_menu_open = false
    }
    else {
        $('#account__menu').css({'opacity': 1, 'display': 'flex'})
        $('#account__menu').addClass('visible')
        is_menu_open = true
    }
})


$("#close__account__menu").click(() => {
    $('#account__menu').css({'opacity': 0, 'display': 'none'})
    $('#account__menu').removeClass('visible')
    is_menu_open = false
})


document.addEventListener('click', function(event) {
    let element = document.getElementById('account__menu')
    let account_icon = document.getElementById('account')

    if (!element.contains(event.target) && is_menu_open && !account_icon.contains(event.target)) {
        $('#account__menu').css({'opacity': 0, 'display': 'none'})
        $('#account__menu').removeClass('visible')
        is_menu_open = false
    }
});
