/*jshint esversion: 10 */
/*jshint -W033 */

const newReviewForm = $('#newUserReview > form')
const reviewContent = $('#id_review_content')
const reviewSubmit = $('#reviewSubmitButton')
const editReview = $('#editReview')
const categories = ['implant', 'app', 'upgrade']
const filterActive = 'js-product-filter-button__active'

/**
 * Enables form to add or edit review.
 */
const enableReviewForm = () => {
	reviewContent.removeAttr('disabled')
	reviewSubmit.parent().addClass('d-block')
	newReviewForm.addClass('d-block')
	editReview.attr('id', 'cancelEditReview').removeClass('far fa-edit').addClass('fas fa-times')
}

/**
 * Disables form to add or edit review.
 */
const disableReviewForm = () => {
	reviewContent.attr('disabled', 'true')
	reviewSubmit.parent().removeClass('d-block')
	newReviewForm.removeClass('d-block')
	$('#cancelEditReview').attr('id', 'editReview').removeClass('fas fa-times').addClass('far fa-edit')
}

const getFilterId = () => {
	return _this.attr('id')
}

const clearFilter = () => {
	categories.forEach(cat => {
		$(`.js-filter-${cat}`).removeClass('d-none')
		$(`#${cat}`).removeClass(filterActive)
		$('#clearFilter').addClass('text-muted')
	})
}

const filterById = id => {
	categories.forEach(cat => {
		if (cat == id) {
			$(`.js-filter-${cat}`).removeClass('d-none')
			$(`#${cat}`).addClass(filterActive)
		} else {
			$(`.js-filter-${cat}`).addClass('d-none')
			$(`#${cat}`).removeClass(filterActive)
		}
	})
	$('#clearFilter').removeClass('text-muted')
}

document.querySelectorAll('.product-filter-button').forEach(element => {
	element.addEventListener('click', function (e) {
		e.preventDefault()
		_this = $(this)
		filterId = getFilterId()
		filterById(filterId)
	})
})

$('#clearFilter').click((e) => {
	e.preventDefault();
	clearFilter()
})



$(document).ready(function () {
	$(document).on('click', '#editReview', function () {
		enableReviewForm()
	})
	$(document).on('click', '#cancelEditReview', function () {
		disableReviewForm()
	})
})
