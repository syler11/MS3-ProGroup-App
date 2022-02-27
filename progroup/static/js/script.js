// Initialize the materialize js componenets

$(document).ready(function() {
    $("#copyright").text(new Date().getFullYear());
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    $('.datepicker').datepicker({
        format: "dd/mm/yyyy",
        autoClose: true,
        minDate: new Date(),
    });
    $('select').formSelect();

validateMaterializeSelect();
function validateMaterializeSelect() {
    let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
    let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
    if ($("select.validate").prop("required")) {
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}

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

document.getElementById("greeting").innerHTML = greeting;
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
