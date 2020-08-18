/*jshint esversion: 10 */
/*jshint -W033 */

const profileNavItems = {
	'profile_personal': 'Personal info',
	'profile_support': 'Tech support',
	'profile_bookings': 'Bookings',
	'profile_orders': 'Order History'
}
const profileTitle = $('.profiles-card-title')
let windowUrl = document.location.href

/**
 * Check the value of the clicked nav item and return a matching ID
 * @returns {string} matches id of html element
 */
const getNavId = (el) => {
	for (const [key, value] of Object.entries(profileNavItems)) {
		if (el === value) {
			return key
		}
	}
}

/**
 * Shows the page matching the element ID
 * @param {string} navId takes the value returned from checkNavClicked
 */
const showPage = (navId, titleText) => {
	$(`#${navId}`).removeClass('d-none').addClass('d-block')
	profileTitle.text(titleText)
}

/**
 * Hides the pages that don't match the element ID
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
 * Adds a hash to the address bar
 * @param {string} url the address to add
 */
const updateUrl = (url) => {
	window.location.hash = url
}

/**
 * Adds a click event listener to all profile nav links
 */
document.querySelectorAll('.profile-nav-link').forEach(element => {
	element.addEventListener('click', function (e) {
		e.preventDefault()
		_this = $(this)
		navId = getNavId(_this.children().text())
		title = _this.text()
		_this.addClass('nav-link-active')
		_this.siblings().removeClass('nav-link-active')
		// showPage(navId, title)
		// hidePages(navId)
		$('#dashboardNavbarToggler').collapse('hide')
		splitId = navId.split('_')
		updateUrl(splitId[1])
	})
})

/**
 * Gets the address bar url and splits at hash
 * @returns {string} the portion after the hash
 */
const getUrl = () => {
	fullUrl = document.location.href
	splitUrl = fullUrl.split("#")
	return splitUrl[1]
}

/**
 * Compares the url against array of possible matches and pushes the matching
 * key and value to an array
 * @param {string} url value to compare
 * @return {array} matching values to change displayed page
 */
const compareUrl = (url) => {
	data = []
	for (const [key, value] of Object.entries(profileNavItems)) {
		if (key.includes(url) === true) {
			data.push(key)
			data.push(value)
		}
	}
	return data
}

/**
 * Check if on the profile root page and if so show the personal info section
 * @param {string} windowUrl the full url
 * @param {string} currentUrl the hash split url
 * @return {string} the value of the page to be loaded
 */
const checkProfileRoot = (windowUrl, currentUrl) => {
	if (windowUrl.includes('#') === false) {
		return 'personal'
	} else {
		return currentUrl
	}
}

/**
 * Processes hash changes in the url and updates page content
 */
const hashUpdate = () => {
	let hash = window.location.hash
	windowUrl = document.location.href
	splitHash = hash.split('#')
	currentHash = checkProfileRoot(windowUrl, splitHash[1])
	currentPage = compareUrl(currentHash)
	showPage(currentPage[0], currentPage[1])
	hidePages(currentPage[0])
}

/**
 * If page is accessed by url, still display the correct content
 */
const loadByUrl = () => {
	currentUrl = getUrl()
	currentHash = checkProfileRoot(windowUrl, currentUrl)
	currentPage = compareUrl(currentHash)
	showPage(currentPage[0], currentPage[1])
	hidePages(currentPage[0])
	windowUrl = document.location.href
}

$(window).on('hashchange', hashUpdate)

$(document).ready(function () {
	loadByUrl()
})

