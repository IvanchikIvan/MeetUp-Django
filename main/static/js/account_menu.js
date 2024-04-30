"use strict";

let is_menu_open = false

$("#account").click(() => {
    if (is_menu_open) {
<<<<<<< HEAD
        $('#account__menu').css({ 'opacity': 0, 'display': 'none' })
=======
        $('#account__menu').css({'opacity': 0, 'display': 'none'})
>>>>>>> 98fd232f868e088baf30d1c41b8f43f1ab3cd5cc
        $('#account__menu').removeClass('visible')
        is_menu_open = false
    }
    else {
<<<<<<< HEAD
        $('#account__menu').css({ 'opacity': 1, 'display': 'flex' })
=======
        $('#account__menu').css({'opacity': 1, 'display': 'flex'})
>>>>>>> 98fd232f868e088baf30d1c41b8f43f1ab3cd5cc
        $('#account__menu').addClass('visible')
        is_menu_open = true
    }
})


$("#close__account__menu").click(() => {
<<<<<<< HEAD
    $('#account__menu').css({ 'opacity': 0, 'display': 'none' })
=======
    $('#account__menu').css({'opacity': 0, 'display': 'none'})
>>>>>>> 98fd232f868e088baf30d1c41b8f43f1ab3cd5cc
    $('#account__menu').removeClass('visible')
    is_menu_open = false
})


<<<<<<< HEAD
document.addEventListener('click', function (event) {
    let element = document.getElementById('account__menu')
    let account_icon = document.getElementById('account')
    if (element != null) {
        if (!element.contains(event.target) && is_menu_open && !account_icon.contains(event.target)) {
            $('#account__menu').css({ 'opacity': 0, 'display': 'none' })
            $('#account__menu').removeClass('visible')
            is_menu_open = false
        }
=======
document.addEventListener('click', function(event) {
    let element = document.getElementById('account__menu')
    let account_icon = document.getElementById('account')

    if (!element.contains(event.target) && is_menu_open && !account_icon.contains(event.target)) {
        $('#account__menu').css({'opacity': 0, 'display': 'none'})
        $('#account__menu').removeClass('visible')
        is_menu_open = false
>>>>>>> 98fd232f868e088baf30d1c41b8f43f1ab3cd5cc
    }
});
