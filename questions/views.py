from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from products.models import Product
from .models import UserQuestion, OwnerReply
from .forms import OwnerReplyForm


def questions(request):
    
    answer_form = OwnerReplyForm()
    unanswered_questions = UserQuestion.objects.filter(has_answer=False)
    answered_questions = UserQuestion.objects.filter(has_answer=True)
    print(f'answered_questions: {answered_questions}')

    context = {
        'unanswered_questions': unanswered_questions,
        'answered_questions': answered_questions,
        'answer_form': answer_form,
    }

    return render(request, 'questions/questions.html', context)

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
            messages.info(request, 'Your question has been added successfully!')
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
            messages.info(request, 'Your reply has been added successfully!')
        except Exception as e:
            print(f'There was an error: {e}')

    return redirect(request.META['HTTP_REFERER'])
