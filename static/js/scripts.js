/*jshint esversion: 10 */
/*jshint -W033 */

$('.toast').toast('show')

$('.toast-close').click(() => {
	$('.toast').toast('hide')
})
