// calculation.js will execute simply calculations for user
//to provide values for the database such total rooms and total PAX

// The line of code was added below to avoid linting error in JS Hint
var $ = window.$;

function calculateTotalPax() {
  // will calculate the total nmber of people by suming the values from all room types
  var room_occupancy={
    single: 1,
    double: 2,
    twin: 2,
    triple: 3    
  };

  var occupancy={};
  
  occupancy.single = ($("#single_room").val() * room_occupancy.single );
  occupancy.double = ($("#double_room").val() * room_occupancy.double );
  occupancy.twin = ($("#twin_room").val() * room_occupancy.twin );
  occupancy.triple = ($("#triple_room").val() * room_occupancy.triple );
  
  var total = occupancy.single + occupancy.double+ occupancy.twin + occupancy.triple;

  $("#pax").val(total);
  
}

$(function()
// will display result from calculateTotalPax on keyup
 {
    $(".validate").on("change keyup",calculateTotalPax);
});

function calculateTotalRooms() {
// will calculate the total nmber of rooms by suming the values from all room types
  var room = {};

  room.single = $("#single_room").val()*1;
  room.double = $("#double_room").val()*1;
  room.twin = $("#twin_room").val()*1;
  room.triple = $("#triple_room").val()*1;
  
  var totals = room.single + room.double + room.twin + room.triple;

  $("#rooms").val(totals);

}

$(function()
// will display result from calculateTotalRooms on keyup
 {
    $(".validate").on("change keyup",calculateTotalRooms);
});