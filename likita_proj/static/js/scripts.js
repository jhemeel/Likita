// typewrite

var colours = ["#1a54b0", "#6109ad", "#838303;", "orange", "#1cad6e"]

class TxtType {
  constructor(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = "";
    this.tick();
    this.isDeleting = false;
  }
  tick() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];

    if (this.isDeleting) {
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    // this.el.innerHTML = '<span class="wrap">' + this.txt + "</span>";
    this.el.innerHTML = '<span class="wrap" style="color: ' + colours[i] + '">'+this.txt+'</span>';

    var that = this;
    var delta = 200 - Math.random() * 100;

    if (this.isDeleting) {
      delta /= 2;
    }

    if (!this.isDeleting && this.txt === fullTxt) {
      delta = this.period;
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === "") {
      this.isDeleting = false;
      this.loopNum++;
      delta = 500;
    }

    setTimeout(function () {
      that.tick();
    }, delta);
  }
}

window.onload = function () {
  var elements = document.getElementsByClassName("typewrite");
  for (var i = 0; i < elements.length; i++) {
    var toRotate = elements[i].getAttribute("data-type");
    var period = elements[i].getAttribute("data-period");
    if (toRotate) {
      new TxtType(elements[i], JSON.parse(toRotate), period);
    }
  }
  // INJECT CSS
  var css = document.createElement("style");
  css.type = "text/css";
  css.innerHTML =
    ".typewrite > .wrap {padding-right: 5px; border-right: 0.2rem solid var(--primary-color); color: var(--primary-color, )}";
  document.body.appendChild(css);
};


// carousels for post images

// function autoplayCarousel() {
//     const carouselEl = document.getElementById("carousel");
//     const slideContainerEl = carouselEl.querySelector("#slide-container");
//     const slideEl = carouselEl.querySelector(".slide");
//     let slideWidth = slideEl.offsetWidth;
//     // Add click handlers
//     document.querySelector("#back-button")
//         .addEventListener("click", () => navigate("backward"));
//     document.querySelector("#forward-button")
//         .addEventListener("click", () => navigate("forward"));
//     document.querySelectorAll(".slide-indicator")
//         .forEach((dot, index) => {
//             dot.addEventListener("click", () => navigate(index));
//             dot.addEventListener("mouseenter", () => clearInterval(autoplay));
//         });
//     // Add keyboard handlers
//     document.addEventListener('keydown', (e) => {
//         if (e.code === 'ArrowLeft') {
//             clearInterval(autoplay);
//             navigate("backward");
//         } else if (e.code === 'ArrowRight') {
//             clearInterval(autoplay);
//             navigate("forward");
//         }
//     });
//     // Add resize handler
//     window.addEventListener('resize', () => {
//         slideWidth = slideEl.offsetWidth;
//     });
//     // Autoplay
//     const autoplay = setInterval(() => navigate("forward"), 3000);
//     slideContainerEl.addEventListener("mouseenter", () => clearInterval(autoplay));
//     // Slide transition
//     const getNewScrollPosition = (arg) => {
//         const gap = 10;
//         const maxScrollLeft = slideContainerEl.scrollWidth - slideWidth;
//         if (arg === "forward") {
//             const x = slideContainerEl.scrollLeft + slideWidth + gap;
//             return x <= maxScrollLeft ? x : 0;
//         } else if (arg === "backward") {
//             const x = slideContainerEl.scrollLeft - slideWidth - gap;
//             return x >= 0 ? x : maxScrollLeft;
//         } else if (typeof arg === "number") {
//             const x = arg * (slideWidth + gap);
//             return x;
//         }
//     }
//     const navigate = (arg) => {
//         slideContainerEl.scrollLeft = getNewScrollPosition(arg);
//     }
//     // Slide indicators
//     const slideObserver = new IntersectionObserver((entries, observer) => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting) {
//                 const slideIndex = entry.target.dataset.slideindex;
//                 carouselEl.querySelector('.slide-indicator.active').classList.remove('active');
//                 carouselEl.querySelectorAll('.slide-indicator')[slideIndex].classList.add('active');
//             }
//         });
//     }, { root: slideContainerEl, threshold: .1 });
//     document.querySelectorAll('.slide').forEach((slide) => {
//         slideObserver.observe(slide);
//     });
// }
// autoplayCarousel();