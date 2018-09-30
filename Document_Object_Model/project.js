var button = document.querySelector("#restart")
var allCells = document.querySelectorAll("td")

// Restart table
button.addEventListener("click", function(){
  for (var i = 0; i < allCells.length; i++) {
    allCells[i].textContent = ""
  }
})

// Change marker function
function change() {
  if (this.textContent == "X") {
    this.textContent = "O"
  } else if (this.textContent == "O") {
    this.textContent = ""
  }else {
    this.textContent = "X"
  }
}

// Change marker
for (var i = 0; i < allCells.length; i++) {
  allCells[i].addEventListener("click", change)
}
