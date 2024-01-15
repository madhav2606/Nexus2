const mainMenu = document.querySelector('.nav-menu');
const closeMenu = document.querySelector('.closeMenu');
const openMenu = document.querySelector('.openMenu');


openMenu.addEventListener('click',show);
closeMenu.addEventListener('click',close);

function show(){
    mainMenu.style.display = 'flex';
    mainMenu.style.backgroundColor='white';
    mainMenu.style.top = '0';
}
function close(){
    mainMenu.style.top = '-10000%';
}

