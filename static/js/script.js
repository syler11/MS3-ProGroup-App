$(document).ready(function() {
    $("#copyright").text(new Date().getFullYear());
    $('.collapsible').collapsible();
});

var today = new Date();

// Display full date and greets the session user accoring to teh time of the day
function dateGreeting() {
var day = today.getDate();
var monthNames = [ "January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December" ];
var month = monthNames[today.getMonth()];
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
document.getElementById("txtDate").innerHTML = day;
document.getElementById("txtMonth").innerHTML = month;
document.getElementById("txtYear").innerHTML = year;
}

// Dispaly counting clock
window.onload = displayClock();
function displayClock(){
    var days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var dayFull = days[today.getDay()];
    var clock = new Date().toLocaleTimeString();
  document.getElementById("txtTime").innerHTML = dayFull +', ' + clock;
  setTimeout(displayClock, 1000); 
}

dateGreeting();