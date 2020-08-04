from django.shortcuts import render


def products(request):
    """
    Returns a view with all products displayed.
    """
    return render(request, 'products.html')
