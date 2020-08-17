/*jshint esversion: 10 */
/*jshint -W033 */

const profileNavItems = {
	'profilePersonalInfo': 'Personal info',
	'profileTechSupport': 'Tech support',
	'profileBookings': 'Bookings',
	'profileOrderHistory': 'Order History'
}
const profileTitle = $('.profiles-card-title')

/**
 * Check the value of the clicked nav item and return a matching ID
 * @returns {string} matches id of html element
 */
const getNavId = () => {
	for (const [key, value] of Object.entries(profileNavItems)) {
		if (_this.children().text() === value) {
			return key
		}
	}
}

/**
 * Shows the page matching the clicked element
 * @param {string} navId takes the value returned from checkNavClicked
 */
const showPage = (navId, titleText) => {
	$(`#${navId}`).removeClass('d-none').addClass('d-block')
	profileTitle.text(titleText)
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
		navId = getNavId()
		title = _this.text()
		_this.addClass('nav-link-active')
		_this.siblings().removeClass('nav-link-active')
		showPage(navId, title)
		hidePages(navId)
		$('#dashboardNavbarToggler').collapse('hide')
	})
})
