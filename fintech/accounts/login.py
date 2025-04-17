from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .mailer_otp import send_otp
from .models import TwoFactorModel

User = get_user_model()

class LoginView(View):
    def get(self, request):
        # Render the login template for GET requests
        return render(request, 'base/login.html')
    
    def post(self, request):
        # Extract data from the POST request
        email = request.POST.get('email')
        password = request.POST.get('password')
        account_type = request.POST.get('account_type')

        # Basic validation
        if not ({email,password,account_type}):
            return JsonResponse({'error': 'Please all fields are required'}, status=400)

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        # If authentication fails, check if the input is an email and try again
        if user is not None:
            if user.account_type != account_type:
                return JsonResponse({'error': f"You are not allowed to log in as a {account_type.capitalize()} Account"}, status=400)
            
            if not user.email_varified:

                send_otp(user.email)
                return JsonResponse({'verify': 'email not Verified A new notification has been sent to your email'}, status=400)
            try:
                 userTwofa = TwoFactorModel.objects.get(user=user)
                 if userTwofa.is_twofactor_enabled:
                     return JsonResponse({'twofactor': '2FA Verification Is Rquired'})
            except: TwoFactorModel.DoesNotExist  
            login(request, user)
            return JsonResponse({'success': 'Log in successful'}, status=200)
        
        else:
         return JsonResponse({'error': 'invalid email or password'}, status=400)


        
