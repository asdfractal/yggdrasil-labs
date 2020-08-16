from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

from checkout.models import Order
from bookings.models import Booking
from .models import UserProfile
from .forms import UserProfileForm, TechSupportForm


def profile(request):
    """
    Display the users profile, bookings and order history. Processes updates to
    user information and submission of tech support form.
    """
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    form_profile = UserProfileForm(instance=user_profile)
    bookings = Booking.objects.filter(user_profile=user_profile)
    orders = Order.objects.filter(user_profile=user_profile)
    form_tech = TechSupportForm()
    is_client = user_profile.is_client
    if request.method == "POST":
        if UserProfileForm().prefix in request.POST:
            form_profile = UserProfileForm(request.POST, instance=user_profile)
            if form_profile.is_valid():
                form_profile.save()
                messages.success(request, "Profile updated.")
            else:
                messages.error(request, "Error updating profile.")

        elif TechSupportForm().prefix in request.POST:
            form_tech = TechSupportForm(request.POST)
            if form_tech.is_valid():
                user_email = user.email
                subject = request.POST.get("form_tech-subject", "")
                content = request.POST.get("form_tech-content", "")
                email_template = get_template("profiles/tech-support-email.txt")
                email_context = {
                    "subject": subject,
                    "content": content,
                }
                email_content = email_template.render(email_context)
                email = EmailMessage(
                    "Tech Support",
                    email_content,
                    to=["tech.support@yggdrasillabs.com"],
                    headers={"Reply-to": user_email},
                )
                try:
                    email.send()
                    messages.success(
                        request,
                        "Message sent. We will get back to you as soon as possible.",
                    )
                    return redirect("profile")
                except Exception as e:
                    messages.error(request, f"Message not sent, error! {e}")
                    return redirect("profile")
            else:
                messages.error(request, "Error sending message.")

    context = {
        "profile": user_profile,
        "form_profile": form_profile,
        "is_client": is_client,
        "form_tech": form_tech,
        "bookings": bookings,
        "orders": orders,
    }

    return render(request, "profiles/dashboard.html", context)
