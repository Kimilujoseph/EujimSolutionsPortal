# utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


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

def send_suspension_email(user, request, suspension_reason=None):
    context = {
        'user': user,
        'suspension_reason': suspension_reason or "Violation of terms of service",
        'suspension_date': timezone.now().strftime("%B %d, %Y"),
        'support_email': settings.SUPPORT_EMAIL,
        'site_url': settings.FRONTEND_URL
    }

    html_content = render_to_string('emails/account_suspended.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=f"Account Suspension Notice - {settings.SITE_NAME}",
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_unsuspension_email(user, request):
    context = {
        'user': user,
        'reinstatement_date': timezone.now().strftime("%B %d, %Y"),
        'login_url': f"{settings.FRONTEND_URL}/login",
        'support_email': settings.SUPPORT_EMAIL,
        'site_url': settings.FRONTEND_URL
    }

    html_content = render_to_string('emails/account_unsuspended.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=f"Account Reinstated - {settings.SITE_NAME}",
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_password_reset_email(user, request, token):
    current_site = get_current_site(request)
    reset_url = request.build_absolute_uri(
        reverse('password-reset-confirm', kwargs={'uid': user.id, 'token': token})
    )
    
    context = {
        'user': user,
        'reset_url': reset_url,
        'site_name': current_site.name,
    }
    
    html_content = render_to_string('emails/password_reset_email.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject="Reset Your Password",
        body=text_content,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_password_reset_confirmation_email(user):
    from django.template.loader import render_to_string
    from django.utils.html import strip_tags
    from django.core.mail import EmailMultiAlternatives

    context = {
        'user': user,
        'site_name': "YourSiteName",  # You can make this dynamic if needed
    }

    html_content = render_to_string('emails/password_reset_confirm.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject="Your Password Has Been Reset",
        body=text_content,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

