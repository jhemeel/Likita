
const chat = document.querySelector(".chat")
function showChat() {
  if (chat){
    chat.addEventListener("click", () => {
      document.querySelector("aside").classList.toggle("shows");
    });
  }
  
}
showChat();
