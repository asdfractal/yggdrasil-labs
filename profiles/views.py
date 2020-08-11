from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage

from .models import UserProfile
from .forms import UserProfileForm, TechSupportForm


def profile(request):
    """
    Display the users profile.
    """
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    form_profile = UserProfileForm(instance=user_profile)
    form_tech = TechSupportForm()
    is_client = user_profile.is_client
    if request.method == "POST":
        if UserProfileForm().prefix in request.POST:
            print("profile form")
            form_profile = UserProfileForm(request.POST, instance=user_profile)
            if form_profile.is_valid():
                form_profile.save()
        elif TechSupportForm().prefix in request.POST:
            print("tech form")
            print(user.email)
            form_tech = TechSupportForm(request.POST)
            if form_tech.is_valid():
                print("form valid")
                user_email = user.email
                subject = request.POST.get("form_tech-subject", "")
                content = request.POST.get("form_tech-content", "")
                email_template = get_template("profiles/tech-support-email.txt")
                email_context = {
                    "user_email": user_email,
                    "subject": subject,
                    "content": content,
                }
                print("context")
                print(email_context)
                email_content = email_template.render(email_context)
                email = EmailMessage(
                    "test",
                    email_content,
                    to=["james.fractal@gmail.com"],
                    headers={"Reply-to": user_email},
                )
                email.send()
                print(email)
                return redirect("profile")

    context = {
        "profile": user_profile,
        "form_profile": form_profile,
        "is_client": is_client,
        "form_tech": form_tech,
    }
    print(is_client)

    return render(request, "profiles/dashboard.html", context)
