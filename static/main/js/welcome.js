const contactDiv = document.querySelector('.contact-div')


window.addEventListener('click', function(event){
    if (event.target.closest('.get-contact-list')){
        event.preventDefault()
        contactDiv.classList.remove('none')
    } else {
        contactDiv.classList.add('none')
    }
})