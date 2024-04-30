"use strict";

let menu_open = false


$("#menu").click(() => {
<<<<<<< HEAD
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
=======
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
>>>>>>> 98fd232f868e088baf30d1c41b8f43f1ab3cd5cc
});


$("#meets_icon").click(() => {
<<<<<<< HEAD
  $('#meets_icon').toggleClass("meets_icon-open")
  $('#meets__nav').toggleClass("meets__nav-close")
  $('#meets__nav').toggleClass("meets__nav-open")
});


const navItems = document.querySelectorAll('.nav__item'); // Выбираем все элементы навигации
const currentUrl = window.location.pathname; // Получаем URL текущей страницы

navItems.forEach(item => { // Проходим по каждому элементу навигации
  const link = item.querySelector('a'); // Получаем ссылку внутри элемента

  if (link && link.getAttribute('href') === currentUrl) { // Если ссылка есть и её URL совпадает с текущим
    item.classList.add('active'); // Добавляем класс active
    item.classList.remove('noactive'); // Удаляем класс noactive
  } else {
    item.classList.add('noactive'); // Добавляем класс noactive
    item.classList.remove('active'); // Удаляем класс active
  }
});
=======
    $('#meets_icon').toggleClass("meets_icon-open")
    $('#meets__nav').toggleClass("meets__nav-close")
    $('#meets__nav').toggleClass("meets__nav-open")
});
>>>>>>> 98fd232f868e088baf30d1c41b8f43f1ab3cd5cc
