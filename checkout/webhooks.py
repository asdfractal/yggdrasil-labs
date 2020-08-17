import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWebhookHandler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for Stripe webhooks.
    """
    # Setup
    wh_secret = settings.STRIPE_WEBHOOK_SECRET
    wh_secret_local = "whsec_0XfQFIdIGmEhnTT4XZ5eCS6O9KjStjXq"
    wh_secret_ng = "whsec_P7VaJs1ku70PPwbx794ttb5M06rzbArM"
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    # stripe.Event.construct_from(json.loads(payload), wh_secret_ng)
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        # Invalid payload
        print("value error")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print(f"invalid signature | {e}")
        print(f"sig: {sig_header}")
        return HttpResponse(status=400)
    except Exception as e:
        print(f"other {e}")
        return HttpResponse(content=e, status=400)

    handler = StripeWebhookHandler(request)
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_payment_failed,
    }
    event_type = event["type"]
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)
    return response
