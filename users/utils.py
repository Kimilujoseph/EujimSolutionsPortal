# utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_verification_email(user, request):
    verification_url = request.build_absolute_uri(
        f"/verify-email/{user.id}/{user.verificationCode}/"
    )
    
    context = {
        'user': user,
        'verification_url': verification_url
    }
    
    html_content = render_to_string('emails/verification_email.html', context)
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(
        subject="Verify Your Email Address",
        body=text_content,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_confirmation_email(user):
    context = {'user': user}
    
    html_content = render_to_string('emails/verification_success.html', context)
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(
        subject="Email Verification Successful",
        body=text_content,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()