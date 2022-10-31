function hideElement() {
    var x = document.getElementById("bookingForm");
    x.style.display = "none";
}

function createBooking() {
    $.ajax({
        type: "POST",
        url: `add/`,
        data:
        {
            doctor: $("#post-doctor").val(),
            date: $("#post-date").val(),
            time: $("#post-time").val(),
            csrfmiddlewaretoken: "{{ csrf_token }}",
        },
        dataType: "json",
        success: function()
        {
            $.get("/booking/json", function(data) { showMessage(data) })
        },
        error: function(error) { alert("Error happened") },
    })
    return false;   
}

// Delete (cancel) previously booked appointment
function deleteBooking(id) {
    $.ajax({
        type :"DELETE",
        csrfmiddlewaretoken: "{{ csrf_token }}",
        url :`/booking/delete/${id}`,
        success: function()
        {
            $(`#${id}`).remove();
            $.get("/booking/json", function(data) { showMessage(data) })
        },
        error: function(error){ alert("Error happened") },
    })
}

// Show message on how many appointments user have booked
function showMessage(data) {
    if (data.length == 0) {
        $("#messageInfo").html("It seems like you haven't booked any appointment yet!");
        $("#bookingButton").html("START BOOKING HERE");
        $("#appointmentList").hide();
        $(".viewBooking").hide();

    } else {
        $("#messageInfo").html("You have " + data.length + " appointment(s) booked!");
        $("#bookingButton").html("BOOK MORE APPOINTMENTS HERE");
        $("#appointmentList").show();
        $(".viewBooking").show();   
    }
}

function searchDokter(){
    getSearchDokter();
    window.scrollTo(0, $(".card-collection").offset().top);
}

function getSearchDokter(){
    let temp = "";
    $.ajax({
        url: `/booking/all/?search=${$("#search").val()}`,
        type: "GET",
        dataType: "json",
        success: function(data){
            if (data.length!=0) {

                for (let appointment of data){
                    temp += `<div id="${appointment.pk}" class="card shadow mx-4 mb-5 zoom div-booking" style="background-color: #eae7dc; color: #8e8d8a; width: 18rem; border-radius: 25px;"">
                                <div class="card-header div-booking">Appointment ${appointment.pk} ♡ </div>
                                <div class="card-body div-booking">
                                    <p class="card-title lead"><strong>${appointment.fields.doctor}</strong></p>
                                    <p class="card-text lead">Date: ${appointment.fields.date}</p>
                                    <p class="card-text lead">Time: ${appointment.fields.time}</p>
                                </div>
                                <div class="d-flex justify-content-center mx-3 div-booking">
                                    <a onclick="deleteBooking(${appointment.pk})" class="text-underline" style="color: #e85a4f;">Cancel Appointment</a>
                                </div>
                                <h3 class="lead my-3">or</h3>
                                <div class="d-flex justify-content-center mx-3 mb-4 div-booking">
                                    <a onclick="deleteBooking(${appointment.pk})" class="text-underline" style="color: #87ab69;">Mark as Completed</a>
                                </div>
                            </div>`
                }

            } else {
                temp = `<h1 class="text-bold lead pb-3">No appointment with this doctor is found :(</h1>`
            }

            $('.card-collection').html(temp);
        },

        error: function(data){ alert('Error Detected'); }
    })
}

$(document).ready(function() {
    
    $("#appointmentList").hide();

    $("#bookingButton").click(function() {
        $("#bookingForm").show();
    })

    $("#closeButton").click(function() {
        $("#bookingForm").hide();
    })

    $.get("/booking/json", function(data){ showMessage(data) })
    searchDokter();

    var typed = new Typed('#typed', {
        strings: ["♡ ♡"],
        typeSpeed: 200,
        backSpeed: 200,
        backDelay: 200,
        startDelay: 200,
        loop: true,
        });

    var typed_two = new Typed('#typed_two', {
        strings: ["Here is the list of your upcoming appointments!"],
        typeSpeed: 120,
        backSpeed: 120,
        backDelay: 2000,
        startDelay: 500,
        loop: true,
        });

    var typed_three = new Typed('#typed_three', {
        strings: ["♡ ♡"],
        typeSpeed: 200,
        backSpeed: 200,
        backDelay: 200,
        startDelay: 200,
        loop: true,
        });

})