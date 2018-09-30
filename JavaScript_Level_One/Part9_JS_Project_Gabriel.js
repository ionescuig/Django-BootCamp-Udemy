var fname = prompt("First Name")
var lname = prompt("Last Name")
var age = prompt("Age")
var height = prompt("Height (cm)")
var pet = prompt("Pet name")


if ((fname[0] === lname[0]) && ((20 < age) && (age < 30)) && (height >= 170) && (pet.slice(-1) === "y")){
  console.log("You are a spy!");
}
else {
  console.log("Have a nice day!");
}
