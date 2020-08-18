from django.shortcuts import render


def index(request):
    """
    Renders the index view.
    """
    return render(request, "pages/index.html")


def contact(request):
    """
    Renders a view with a form to contact the business.
    """
    context = {
        "page_title": "Contact Us",
    }
    return render(request, "pages/contact.html", context)


def about(request):
    """
    Renders a view with information about the business.
    """
    context = {
        "page_title": "About Us",
    }
    return render(request, "pages/about.html", context)
