from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from products.models import Product
from .models import UserQuestion, OwnerReply
from .forms import UserQuestionForm


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


@login_required
def add_reply(request, question_id):

    if request.method == 'POST':
        content = request.POST['content']
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        question = UserQuestion.objects.get(pk=question_id)

        product_id = question.product.id

        try:
            reply = OwnerReply(
                user = user,
                question = question,
                content = content
            )
            reply.save()
        except Exception as e:
            print(f'There was an error: {e}')
    return redirect(reverse('product_detail', kwargs={'product_id': product_id}))
