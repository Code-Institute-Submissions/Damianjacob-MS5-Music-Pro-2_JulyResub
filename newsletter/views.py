from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

from .models import NewsletterEmail


def newsletter(request):
    template = 'newsletter.html'
    context = {}

    if request.method == 'POST':
        email = request.POST.get('newsletter-email')

        try:
            existing_email = NewsletterEmail.objects.get(email=email)
            if existing_email:
                messages.info(
                    request, 'You are already subscribed to our newsletter!')
        except NewsletterEmail.DoesNotExist:
            try:
                send_mail(
                    'Musicpro Newsletter Confirmation',
                    'Thank you for subscribing to our newsletter!',
                    'newsletter@musicpro.com',
                    [email],
                    fail_silently=False,
                )
                messages.info(
                    request, f'You have successfully subscribed to our\
                        newsletter! A confirmation email has been sent\
                        to {email}')
                NewsletterEmail.objects.create(email=email)
            except Exception as e:
                messages.error(request, f'Sorry, there has been an error:\
                        {e}')

    return render(request, template_name=template, context=context)
