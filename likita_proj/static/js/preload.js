
function startLoader() {
    const loader = document.querySelector(".loading");
  
    setTimeout(function() {
      loader.style.right = "0";
    }, 1000);
  
    window.addEventListener("DOMContentLoaded", function(event) {
      setTimeout(function() {
        loader.style.left = "200%";
        document.body.classList.remove("loading");
      }, 1500);
    });
  }
  
  startLoader();
  