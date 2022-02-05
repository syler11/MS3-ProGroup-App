function calculateTotalPax()
{
  let room_occupancy={
    single: 1,
    double: 2,
    twin: 2,
    triple: 3    
  };

  let occupancy={}
  
  occupancy.single = ($("#single_room").val() * room_occupancy.single )
  occupancy.double = ($("#double_room").val() * room_occupancy.double )
  occupancy.twin = ($("#twin_room").val() * room_occupancy.twin )
  occupancy.triple = ($("#triple_room").val() * room_occupancy.triple )
  
  let total = occupancy.single + occupancy.double+ occupancy.twin + occupancy.triple;

  $("#pax").val(total);
  
}

$(function()
 {
    $(".validate").on("change keyup",calculateTotalPax)
})

function calculateTotalRooms() {

  let room = {}

  room.single = $("#single_room").val()*1
  room.double = $("#double_room").val()*1
  room.twin = $("#twin_room").val()*1
  room.triple = $("#triple_room").val()*1
  
  let totals = room.single + room.double + room.twin + room.triple;

  $("#rooms").val(totals);

}

$(function()
 {
    $(".validate").on("change keyup",calculateTotalRooms)
})