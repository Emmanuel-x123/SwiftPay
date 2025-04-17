import secrets
from django.db import models
from django.contrib.auth.models import AbstractUser
import pyotp
from shortuuid.django_fields import ShortUUIDField
from django.utils.timezone import now
from datetime import timedelta

ACCOUNT_TYPE_CHOICES = [
    ('personal', 'personal'),
    ('business', 'business'),
]


class User(AbstractUser):
    id = ShortUUIDField(primary_key=True,unique=True,editable=False, alphabet='bcarem12345qop09867890')
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=250, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    create_at= models.DateTimeField(auto_now_add=True)
    email_varified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES,default='perdonal')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']

    def __str__(self):
        return self.username


class PersonalAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personalaccount')
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.user.last_name


class BusinessAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='businessaccount')
    date_of_birth = models.DateField()
    company_name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200)
    business_address = models.TextField()
    legal_name= models.CharField(max_length=255)
    logo = models.ImageField(upload_to='business_logos', null=True, blank=True)

    def __str__(self):
        return self.user.last_name       



class OTPCODE(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    phone_otp = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_otp_expired(self):
        if self.created_at is None:
            return True
        return now() > self.created_at + timedelta(minutes=10)    

    def __str__(self):
        return  self.user.email

class TwoFactorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='twofactor')
    is_twofactor_enabled = models.BooleanField(default=False)
    twoFaCode = models.CharField(max_length=200)
    twoFa_created = models.DateTimeField(blank=True, null=True)
    twoFaBackUp = models.JSONField(default=list, blank=True)
    is_email_enabled = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=200, blank=True, null=True)
    email_created = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def generate_twofactor_secret(self):
        if not self.is_twofactor_enabled:
             self.twoFaCode = pyotp.random_base32()
             self.save()


    def generate_twofactor_backup(self):
        self.twoFaBackUp = [secrets.token_hex(4) for _ in range(9)] 
        self.save()