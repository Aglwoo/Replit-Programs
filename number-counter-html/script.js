const number = document.querySelector("#num")
const addButton = document.querySelector("#add1")
const minusButton = document.querySelector("#minus1")


function add() {
  let text = +number.innerText
  text = text + 1
  number.innerText = text
}

function minus() {
  let text = +number.innerText
  text -= 1
  number.innerText = text
}

addButton.addEventListener("click",add)
minusButton.addEventListener("click",minus)