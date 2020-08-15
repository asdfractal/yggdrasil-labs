/*jshint esversion: 10 */
/*jshint -W033 */

const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1)
const clientSecret = $('#id_client_secret').text().slice(1, -1)
const stripe = Stripe(stripePublicKey)
const elements = stripe.elements()
const style = {
	base: {
		color: '#1F1F1F',
		fontFamily: '"Josefin-sans", sans-serif',
		fontSmoothing: 'antialiased',
		fontSize: '1.6rem',
		'::placeholder': {
			color: '#aab7c4'
		}
	},
	invalid: {
		color: '#FF0033',
		iconColor: '#FF0033'
	}
}
const card = elements.create('card', { style: style })
card.mount('#cardElement')
