/* Stripe card element set up and processing */
const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1)
const clientSecret = $("#id_client_secret").text().slice(1, -1)
const stripe = Stripe(stripePublicKey)
const elements = stripe.elements()
const loadingSpinner = $("#loadingOverlay")
const errorElement = document.getElementById("cardErrors")
const form = document.getElementById("paymentForm")
const style = {
	base: {
		color: "#1F1F1F",
		fontFamily: '"Josefin-sans", sans-serif',
		fontWeight: 300,
		fontSmoothing: "antialiased",
		fontSize: "1.2rem",
		"::placeholder": {
			color: "#aab7c4",
		},
	},
	invalid: {
		color: "#FF0033",
		iconColor: "#FF0033",
	},
}
const card = elements.create("card", { style: style })

/**
 * Enables form after an error.
 */
const enableForm = () => {
	loadingSpinner.fadeToggle(100)
	card.update({ disabled: false })
	$("#paymentSubmit").attr("disabled", false)
}

card.mount("#cardElement")

// Handle and display card form error
card.addEventListener("change", (e) => {
	if (e.error) {
		const html = `
                <span role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${e.error.message}</span>
            `
		$(errorElement).html(html)
	} else {
		errorElement.textContent = ""
	}
})

// handle form submit
form.addEventListener("submit", (e) => {
	e.preventDefault()
	card.update({ disabled: true })
	$("#paymentSubmit").attr("disabled", true)
	loadingSpinner.fadeToggle(100)

	const saveInfo = Boolean($("#saveInfo").attr("checked"))
	const csrfToken = $('input[name="csrfmiddlewaretoken"]').val()
	const postData = {
		csrfmiddlewaretoken: csrfToken,
		client_secret: clientSecret,
		save_info: saveInfo,
	}
	const url = "/checkout/cache_checkout_data/"

	$.post(url, postData)
		.done(() => {
			stripe
				.confirmCardPayment(clientSecret, {
					payment_method: {
						card: card,
						billing_details: {
							name: $.trim(form.full_name.value),
							phone: $.trim(form.phone_number.value),
							email: $.trim(form.email.value),
							address: {
								line1: $.trim(form.street_address1.value),
								line2: $.trim(form.street_address2.value),
								city: $.trim(form.city.value),
								state: $.trim(form.state.value),
								country: $.trim(form.country.value),
							},
						},
					},
					shipping: {
						name: $.trim(form.full_name.value),
						phone: $.trim(form.phone_number.value),
						address: {
							line1: $.trim(form.street_address1.value),
							line2: $.trim(form.street_address2.value),
							city: $.trim(form.city.value),
							postal_code: $.trim(form.postcode.value),
							state: $.trim(form.state.value),
							country: $.trim(form.country.value),
						},
					},
				})
				.then((result) => {
					if (result.error) {
						const html = `
						<span role="alert">
							<i class="fas fa-times"></i>
						</span>
						<span>${result.error.message}</span>
					`
						$(errorElement).html(html)
						enableForm()
					} else if (result.paymentIntent.status === "succeeded") {
						form.submit()
					} else {
						const html = `
							<span role="alert">
								<i class="fas fa-times"></i>
							</span>
							<span>An unexpected error has occured. Please contact us for assistance.</span>
						`
						$(errorElement).html(html)
						enableForm()
					}
				})
		})
		.fail(function () {
			location.reload()
		})
})
