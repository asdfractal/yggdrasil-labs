/*jshint esversion: 10 */
/*jshint -W033 */

const bookingForm = $('#bookingForm')
const changeBookingButton = $('#changeBookingButton')
const cancelChangeBookingButton = $('#cancelChangeBookingButton')
const bookingDateInput = $("#id_booking_date")
const bookingTimeInput = $('#id_booking_time')
const baseUrl = "/api/booking/?booking_date__contains="
const bookingErrors = $('#bookingErrors')
const permanentTimes = ['09', '12', '15']
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

document.querySelectorAll('.button-booking-time').forEach(button => {
	button.addEventListener('click', function (e) {
		e.preventDefault()
		bookingTimeInput.attr({ 'value': $(this).text() })
		$('#bookingSubmitButton').removeAttr('disabled')
	})
})

/**
 * Query server for bookings on the selected date
 * @param {string} url base api url to append to
 * @param {string} date date to query
 * @returns {object} JSON data from api
 */
const checkDates = async (url, date) => {
	let query = date.getFullYear() + '-' + '0' + (date.getMonth() + 1) + '-' + date.getDate()
	queryUrl = url + query
	const res = await fetch(queryUrl)
	data = await res.json()
	return data
}

/**
 * Process the api response and update the dom
 * @param {string} url base api url to append to
 * @param {string} date date to query
 */
const processDates = async (url, date) => {
	const data = await checkDates(url, date)
	const bookingQuery = data.objects
	const bookedTimes = []
	bookingQuery.forEach(booking => {
		time = booking.booking_time.slice(0, -6)
		bookedTimes.push(time)
	})
	availableTimes = permanentTimes.filter(time => !bookedTimes.includes(time))
	if (bookingQuery.length === 3) {
		bookingErrors.text('No available bookings on this day. Please make another selection.')
	} else if (bookingQuery.length === 0) {
		document.querySelectorAll('.button-booking-time').forEach(button => {
			button.disabled = false
		})
	} else {
		availableTimes.forEach(time => {
			$(`#${time}`).removeAttr('disabled')
		})
	}
}

/**
 * Disables the time selection buttons before api response and resets time input
 * value to ensure an already booked time is not selected
 */
const disableTimes = () => {
	document.querySelectorAll('.button-booking-time').forEach(el => {
		el.disabled = true
	})
	bookingTimeInput.attr({ 'value': '' })
}

$(document).ready(function () {
	// Initialize datepicker and process input
	bookingDateInput.datepicker({
		minDate: 0, maxDate: "+1M", dateFormat: "dd M, yy", beforeShowDay: $.datepicker.noWeekends, onSelect: (dateText) => {
			selectedDate = new Date(dateText)
			$('.booking-times__wrapper').removeClass('d-none')
			bookingErrors.text('')
			disableTimes()
			processDates(baseUrl, selectedDate)
		}
	})
})
