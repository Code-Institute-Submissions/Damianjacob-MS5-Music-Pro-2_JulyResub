from django.shortcuts import render


def index(request):
    """Returns the products page"""

    return render(request, 'home/index.html')
