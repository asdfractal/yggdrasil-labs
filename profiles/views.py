from django.shortcuts import render, get_object_or_404


from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """
    Display the users profile.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)
    context = {
        "profile": user_profile,
        "form": form,
    }

    return render(request, "profiles/dashboard.html", context)
