from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .mailer_otp import send_otp

User = get_user_model()

class RegisterView(View):
    def get(self, request):
        return render(request, 'base/signup.html')
    
    def post(self, request):
       username = request.POST['username']
       email  = request.POST['email']
       phone = request.POST['phone']
       password = request.POST['password']
       password2 = request.POST['password2']
       account_type = request.POST['account_type']


       if not username or not email or not phone or not password or not password2 :
           return JsonResponse({'error': 'please fill the form fields'}, status= 400)
       
       if password != password2:
           return JsonResponse({'error': 'password did not match'}, status= 400)
       
       if User.objects.filter(email=email).exists():
           return JsonResponse({'error': 'Email already exist'}, status= 400)
       
       if User.objects.filter(username=username).exists():
           return JsonResponse({'error': 'Username already exist'}, status= 400)
       
       if User.objects.filter(phone=phone).exists():
           return JsonResponse({'error': 'Phone Number already exist'}, status= 400)
       
       
       user = User.objects.create(
           username = username,
           email = email,
           phone = phone,
           account_type = account_type,
           password = make_password(password)
       )
       send_otp(email)
       return JsonResponse({'success': 'user registration is successful'}, status=201)
    