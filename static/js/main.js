var menu_icon = document.getElementsByClassName("hamburger");
var menu_icon = document.getElementById("menu-icon");
var close_icon = document.getElementById("close-icon");
var navbar = document.getElementById("navbar-toggle");

var width = window.innerWidth;

menu_icon.addEventListener("click", function(){
    menu_icon.style.display = "none";
    close_icon.style.display = "block";
    navbar.style.height = "50vh";
});

close_icon.addEventListener("click", function(){
    menu_icon.style.display = "block";
    close_icon.style.display = "none";
    navbar.style.height = "0vh";
});


//navbar on scroll background

window.addEventListener('scroll', function () {
    const header = document.getElementById('navbar');
    if (window.scrollY > 15) { // Adjust the scroll value as needed
        header.style.background = 'rgb(var(--background-color))';
    } else {
        header.style.background = 'transparent';
    }
});



// dark mode

const body = document.querySelector('body');
const toggle = document.getElementById('background-btn');

let getMode = localStorage.getItem('mode');
console.log(getMode);
if(getMode && getMode === "dark"){
    body.classList.add('dark-mode');
    toggle.classList.add('flipped');
}

toggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    toggle.classList.toggle('flipped');

    if(!body.classList.contains('dark-mode')){
        return localStorage.setItem('mode', 'light');
    }
    return localStorage.setItem('mode', 'dark');
});  
