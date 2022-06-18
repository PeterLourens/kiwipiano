
const navLinkBtns = document.getElementsByClassName(''.nav-link');

for(let i=0; i<navLinkBtns.length; i++) {
    navLinkBtns[i].addEventListener('click', (e) => {

        navLinkBtns.classList.add('active');

    });
};