/*jshint esversion: 10 */
/*jshint -W033 */

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
	$('.datepicker').datepicker();
	$('.timepicker').timepicker();
})
