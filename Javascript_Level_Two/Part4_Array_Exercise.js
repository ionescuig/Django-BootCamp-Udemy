// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
  roster.push(name)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(name) {
  var index = roster.indexOf(name)
  roster.splice(index, 1)
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
  console.log(roster);
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
while (true) {
  var choice = prompt("Please select an option: add, remove, display or quit:")
  if (choice == 'add'){
    var name = prompt("Please enter student name:")
    addNew(name)
  } else if (choice == 'remove') {
    var name = prompt("Please enter student name:")
    remove(name)
  } else if (choice == 'display') {
      console.log(roster);
    } else if (choice == 'quit') {
      alert('Thank you for using our roster!')
      break
    }
  }
