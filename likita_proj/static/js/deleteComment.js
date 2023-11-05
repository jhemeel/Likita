

window.addEventListener("DOMContentLoaded", () => {
    let modal = document.querySelector(".modal");
let cancel = document.querySelector(".cancel");
let buttons = document.querySelectorAll(".modal-btn");

for (var i = 0; i < buttons.length; i++){
    let button = buttons[i]
    button.setAttribute('id', i + 1)

    const deleteCommentModalhandler = () => {
        if (button){
            button.addEventListener("click", () => {
                modal.style.display = "block";
              });
        }
       
        if (cancel){
            cancel.addEventListener("click", () => {
                modal.style.display = "none";
              });
        }
    }
    deleteCommentModalhandler()
}
})




