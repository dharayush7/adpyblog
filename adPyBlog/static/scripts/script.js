const alartBlocks = document.querySelectorAll(".alart-block");
const alartBtns = document.querySelectorAll(".alart-btn");

console.log(alartBlocks);

for (let i = 0; i < alartBtns.length; i++) {
  alartBtns[i].addEventListener("click", () => {
    alartBlocks[i].classList.remove("flex");
    alartBlocks[i].classList.add("hidden");
    alartBtns[i].removeEventListener("click", () => {});
  });
}
