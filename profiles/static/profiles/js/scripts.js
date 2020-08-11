/*jshint esversion: 10 */
/*jshint -W033 */

const profileNavItems = {
	'profilePersonalInfo': 'Personal info',
	'profileTechSupport': 'Tech support',
	'profileBookings': 'Bookings',
	'profileOrderHistory': 'Order History'
}

/**
 * Check the value of the clicked nav item and return a matching ID
 * @returns {string} matches id of html element
 */
const checkNavClicked = () => {
	for (const [key, value] of Object.entries(profileNavItems)) {
		if (_this.text() === value) {
			console.log(key);
			return key
		}
	}
}

/**
 * Shows the page matching the clicked element
 * @param {string} navId takes the value returned from checkNavClicked
 */
const showPage = (navId) => {
	$(`#${navId}`).removeClass('d-none').addClass('d-block')
}

/**
 * Hides the pages that don't match the clicked element
 * @param {string} navId takes the value returned from checkNavClicked
 */
const hidePages = (navId) => {
	for (const key of Object.keys(profileNavItems)) {
		if (navId != key) {
			$(`#${key}`).addClass('d-none').removeClass('d-block')
		}
	}
}

/**
 * Adds a click event listener to all profile nav links
 */
document.querySelectorAll('.profile-nav-link').forEach(element => {
	element.addEventListener('click', function (e) {
		e.preventDefault()
		_this = $(this)
		navId = checkNavClicked()
		showPage(navId)
		hidePages(navId)
	})
})
