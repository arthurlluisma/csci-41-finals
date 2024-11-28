let filterState = false

let filter = document.querySelector(".filter")
let filterHeading = document.querySelector(".filter__heading")
let filterImg = document.querySelector(".filter__img")
let filterTags = document.querySelector(".filter__tags")

filterHeading.addEventListener("click", (evt) => {
  if (!filterState) {
    filterState = true
    filter.style.marginBottom = "2.1rem";
    filterImg.src = "../../../../media/images/arrow-up.svg"
    filterTags.style.display = "flex";
  } else {
    filterState = false
    filter.style.marginBottom = "0";
    filterImg.src = "../../../../media/images/arrow-down.svg"
    filterTags.style.display = "none";
  }
})
