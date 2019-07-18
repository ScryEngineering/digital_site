let menu = document.getElementById('js-menu');
let navToggle = document.getElementById('js-nav-toggle');
navToggle.addEventListener('click', () => {
    menu.classList.toggle('active');
});
const animateBar = (e) => {
    e.classList.toggle("change");
}