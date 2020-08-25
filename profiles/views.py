from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm, TechSupportForm


def profile_login_check(request):
    """
    Checks if the user is authenticated before rendering the profile view in order
    to display a message informing them that login is required and utilize allauth
    next url parameter.
    """
    if not request.user.is_authenticated:
        messages.warning(request, "You must login to view account dashboard.")
    return profile(request)


@login_required
def profile(request):
    """
    Display the users profile, bookings and order history. Processes updates to
    user information and submission of tech support form.
    """
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    form_profile = UserProfileForm(instance=user_profile)
    orders = Order.objects.filter(user_profile=user_profile)
    form_tech = TechSupportForm()
    user_profile.check_personal_key()
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
        "form_tech": form_tech,
        "orders": orders,
        "page_title": "Dashboard",
    }

    return render(request, "profiles/dashboard.html", context)


@login_required
def order_details(request, order_number):
    """
    A view displaying full details of a completed order.
    """
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        "order": order,
        "page_title": "Orders",
    }
    return render(request, "profiles/order-details.html", context)
