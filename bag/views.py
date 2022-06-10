from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """Returns the products page"""
    
    return render(request, 'bag.html')