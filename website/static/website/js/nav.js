document.querySelector("body").addEventListener("wheel", () => {
  let nav = document.querySelector("nav");
  let header = document.querySelector("header");

  let navTitle = document.querySelector(".nav__title");
  let navBtn = document.querySelector(".nav__btn");
  let navUser = document.querySelector(".nav__user");

  if (window.scrollY >= header.offsetTop + header.offsetHeight) {
    nav.style.background = "rgb(255, 255, 255)";
    nav.style.border = "1px solid black";
    navTitle.style.color = "#000";
    navBtn.style.color = "#000";
    navBtn.style.border = "1px solid black";
    navUser.style.color = "#000";
  } else {
    nav.style.background = "transparent";
    nav.style.border = "none";
    navTitle.style.color = "#fff";
    navBtn.style.color = "#fff";
    navBtn.style.border = "1px solid #fff";
    navUser.style.color = "#fff";
  }
});
