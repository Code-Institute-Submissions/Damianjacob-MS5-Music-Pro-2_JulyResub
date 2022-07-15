from email import message
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from products.models import Product
from .models import UserQuestion
from .forms import UserQuestionForm

# Create your views here.

@login_required
def add_question(request, product_id):

    if request.method == 'POST':
        content = request.POST['content']
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        product = Product.objects.get(pk=product_id)

        try:
            question = UserQuestion(
                user = user,
                product = product,
                content = content
            )
            question.save()
        except Exception as e:
            print(f'There was an error: {e}')
    return redirect(reverse('product_detail', kwargs={'product_id': product_id}))