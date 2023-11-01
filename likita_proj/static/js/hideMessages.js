// close messages-box

window.addEventListener("DOMContentLoaded", (event) => {
    close = document.querySelector(".message-close");
    messages = document.querySelector(".messages");
    
    const closeMessages = () => {
        if (close) close.addEventListener('click', ()=>{messages.classList.add('hide-messages')})
    }
    closeMessages()
    
});