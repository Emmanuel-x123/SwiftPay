from django.urls import path

from .home import HomepageView
from .register import RegisterView
from .login import LoginView
from .emailverify import Email_verifyView


urlpatterns = [
   path('', HomepageView.as_view(), name='home'),
   path('register', RegisterView.as_view(), name='register'),  
   path('login', LoginView.as_view(), name='login'),  
   path('email_verify', Email_verifyView.as_view(), name='email_verify'),  
]

