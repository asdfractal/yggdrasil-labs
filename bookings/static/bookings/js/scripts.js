/*jshint esversion: 10 */
/*jshint -W033 */

const bookingForm = $('#bookingForm')
const changeBookingButton = $('#changeBookingButton')
const cancelChangeBookingButton = $('#cancelChangeBookingButton')
const bookingDateInput = $("#id_booking_date")
const bookingTimeInput = $('#id_booking_time')
const baseUrl = "/api/booking/?booking_date__contains="
let selectedDate = new Date()

/* Dynamically displays and hides booking creation form */
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

document.querySelectorAll('.button-booking-time').forEach(el => {
	el.addEventListener('click', function (e) {
		e.preventDefault()
		bookingTimeInput.attr({ 'value': $(this).text() })
		$('#bookingSubmitButton').removeAttr('disabled')
	})
})

const checkDates = async (url, date) => {
	let query = date.getFullYear() + '-' + '0' + (date.getMonth() + 1) + '-' + date.getDate()
	console.log(query)
	queryUrl = url + query
	const res = await fetch(queryUrl)
	data = await res.json()
	console.log(data)
}

$(document).ready(function () {
	bookingDateInput.datepicker({
		minDate: 0, maxDate: "+1M", dateFormat: "dd M, yy", beforeShowDay: $.datepicker.noWeekends, onSelect: (dateText) => {
			// console.log(dateText);
			// bookingDateInput.attr({ 'value': dateText })
			selectedDate = new Date(dateText)
			// console.log(selectedDate);
			checkDates(baseUrl, selectedDate)
		}
	})
})
