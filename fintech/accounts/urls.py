from django.urls import path

from .home import HomepageView
from .register import RegisterView
from .login import LoginView
from .emailverify import Email_verifyView
from .twoFaSetUp import SetUpTwoFa
from .completeTwoFaSetUp import VerifyTwoFaToken
from .twoFaComplete import SetupComplete


urlpatterns = [
   path('', HomepageView.as_view(), name='home'),
   path('register', RegisterView.as_view(), name='register'),  
   path('login', LoginView.as_view(), name='login'),  
   path('email_verify', Email_verifyView.as_view(), name='email_verify'),  
   path('twofa', SetUpTwoFa.as_view(), name='twofa'),
   path('twofaverify', VerifyTwoFaToken.as_view(), name='twofaverify'),
   path('setupComplete', SetupComplete.as_view(), name='setupComplete'),
]

            