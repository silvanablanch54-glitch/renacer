/* ================= SHOW MENU ================= */
const navMenu = document.getElementById('nav-menu'),
    navToggle = document.getElementById('mobile-toggle'),
    navClose = document.getElementById('close-menu')

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu')
    })
}
if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu')
    })
}

/* ================= REMOVE MENU MOBILE ================= */
const navLink = document.querySelectorAll('.nav-link')

function linkAction() {
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/* ================= CHANGE BACKGROUND HEADER ================= */
function scrollHeader() {
    const header = document.getElementById('header')
    if (this.scrollY >= 50) header.classList.add('header-scrolled'); else header.classList.remove('header-scrolled')
}
window.addEventListener('scroll', scrollHeader)

/* ================= SCROLL SECTIONS ACTIVE LINK ================= */
const sections = document.querySelectorAll('section[id]')

function scrollActive() {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop - 100,
            sectionId = current.getAttribute('id')

        let href = document.querySelector('.nav-list a[href*=' + sectionId + ']')
        if (href) {
            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                href.classList.add('active-link')
            } else {
                href.classList.remove('active-link')
            }
        }
    })
}
window.addEventListener('scroll', scrollActive)

/* ================= ANIMATION ON SCROLL ================= */
const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');

const scrollReveal = function () {
    for (let i = 0; i < revealElements.length; i++) {
        const windowHeight = window.innerHeight;
        const elementTop = revealElements[i].getBoundingClientRect().top;
        const elementVisible = 50;

        if (elementTop < windowHeight - elementVisible) {
            revealElements[i].classList.add('active-reveal');
        }
    }
}

window.addEventListener('scroll', scrollReveal);
// Trigger once on load
scrollReveal();
