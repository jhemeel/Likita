


window.addEventListener("DOMContentLoaded", (event) => {
 
  editBtn = document.querySelectorAll(".edit-delete-menu");
edits = document.querySelectorAll(".edit-delete");

function editDelete() {
  editBtn.forEach((btn) => {
    edits.forEach((edit) => {
      if (btn){
        btn.addEventListener("click", () => {
          edit.classList.toggle("shows");
        });
      }
     
    });
  });
}
editDelete();

let caret = document.querySelector(".fa-caret-down");
let hide = document.querySelector(".hide-wrapper");

function caretDown() {
  if (caret){
    caret.addEventListener("click", () => {
      hide.classList.toggle("drops");
    });
  }
 
}
caretDown();
});