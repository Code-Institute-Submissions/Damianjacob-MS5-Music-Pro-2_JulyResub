from django.shortcuts import render


def profile(request):
    """Display user profile"""
    template = 'profile.html'
    context = {}

    return render(request, template, context)