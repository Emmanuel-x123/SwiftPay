from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
import pyotp
from .models import User, OTPCODE

# generate otp codes for users
def generate_otp():
    otpcode = pyotp.TOTP(pyotp.random_base32())
    return otpcode.now()


def send_otp(email):
    subject = 'one time password (OTP) generator'
    otp = generate_otp()
    user = User.objects.get(email=email)
    otp_record, create_otp = OTPCODE.objects.get_or_create(user=user) 
    otp_record.email_otp = otp
    otp_record.created_at = timezone.now()
    otp_record.save()

    # compose the message body 
    body = f"{user.username} your otp verification code is {otp}. this will expire in 10 minutes"
    email_from = settings.EMAIL_HOST_USER
    email_sender = EmailMessage(subject=subject, from_email=email_from, body=body, to=[email])
    email_sender.send(fail_silently=True)