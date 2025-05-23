# utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_verification_email(user, request):
    verification_url = request.build_absolute_uri(
        f"/verify-email/{user.verificationCode}/"
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

def send_approval_email(user, request):
    login_url = request.build_absolute_uri('/login/') 

    context = {
        'user': user,
        'login_url': login_url
    }

    html_content = render_to_string('emails/account_approved.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject="Your Account Has Been Approved",
        body=text_content,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_disapproval_email(user, request):
    context = {
        'user': user
    }

    html_content = render_to_string('emails/account_disapproval.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject="Your Account Has Been Disabled",
        body=text_content,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
