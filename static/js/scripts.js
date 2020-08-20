/*jshint esversion: 10 */
/*jshint -W033 */

$('.toast').toast('show')

$('.toast-close').click(() => {
	$('.toast').toast('hide')
})

$(document).ready(function () {
	$('.index-featured').slick({
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		dots: false,
		autoplay: true,
		autoplaySpeed: 5000,
	});
	$('.index-social-proof').slick({
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		dots: false,
		autoplay: true,
		autoplaySpeed: 10000,
	});
});
