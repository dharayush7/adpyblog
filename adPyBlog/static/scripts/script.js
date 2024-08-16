const alartBlocks = document.querySelectorAll(".alart-block");
const alartBtns = document.querySelectorAll(".alart-btn");

for (let i = 0; i < alartBtns.length; i++) {
  alartBtns[i].addEventListener("click", () => {
    alartBlocks[i].classList.remove("flex");
    alartBlocks[i].style.display = "none";
    alartBtns[i].removeEventListener("click", () => {});
  });
}
