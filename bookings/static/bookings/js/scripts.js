/*jshint esversion: 10 */
/*jshint -W033 */

/* Dynamically displays and hides booking creation form */
bookingForm = $('#bookingForm')
changeBookingButton = $('#changeBookingButton')
cancelChangeBookingButton = $('#cancelChangeBookingButton')

changeBookingButton.click((e) => {
	e.preventDefault()
	bookingForm.removeClass('d-none')
	changeBookingButton.parent().addClass('d-none')
	cancelChangeBookingButton.removeClass('d-none')
})

cancelChangeBookingButton.click((e) => {
	e.preventDefault()
	bookingForm.addClass('d-none')
	changeBookingButton.parent().removeClass('d-none')
	cancelChangeBookingButton.addClass('d-none')
})

$(document).ready(function () {
	$("#id_booking_date").datepicker({ minDate: 0, maxDate: "+1M", showButtonPanel: true, dateFormat: "dd M, yy", beforeShowDay: $.datepicker.noWeekends });
})


// booking api
// let baseUrl = "http://127.0.0.1:8000/api/booking/"

// fetch(baseUrl)
// 	.then(res => res.json())
// 	.then(data => console.log(data))
