$(document).ready(function() {
    $("#copyright").text(new Date().getFullYear());
});

// Display full date and greets the session user accoring to teh time of the day
function dateGreeting() {
var today = new Date();
var day = today.getDate();
var month = today.getMonth();
var year = today.getFullYear();
var hour = today.getHours();
var greeting;

if (hour > 18) {
    greeting = "Good evening, ";
} else if (hour > 12) {
    greeting = "Good afternoon, ";
} else if (hour > 0) {
    greeting = "Good morning, ";
} else {
    greeting = "Welcome"
}

document.getElementById("greeting").innerHTML = greeting + 'Szilard';
document.getElementById("txtDate").innerHTML = 'Date: ' + day + '.' + month+1 + '.' + year;
}

// Dispaly counting clock
window.onload = displayClock();
function displayClock(){
  var clock = new Date().toLocaleTimeString();
  document.getElementById("txtTime").innerHTML = 'Time: ' + clock;
  setTimeout(displayClock, 1000); 
}

dateGreeting();