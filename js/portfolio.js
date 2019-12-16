var menu = document.querySelector('#menu');
var main = document.querySelector('main');
var drawer = document.querySelector('.nav');

menu.addEventListener('click', function (e) {
    drawer.classList.toggle('close');
    e.stopPropagation();
});