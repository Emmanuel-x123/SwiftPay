from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

User = get_user_model()

class LoginView(View):
    def get(self, request):
        # Render the login template for GET requests
        return render(request, 'base/login.html')
    
    def post(self, request):
        # Extract data from the POST request
        email = request.POST['email']
        password = request.POST['password']

        # Basic validation
        if not email or not password:
            return JsonResponse({'error': 'Please provide both email and password'}, status=400)

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        # If authentication fails, check if the input is an email and try again
        if user is None:
            try:
                validate_email(email)  # Check if the input is a valid email
                user = User.objects.filter(email=email).first()
                if user:
                    user = authenticate(request, username=user.username, password=password)
            except ValidationError:
                pass  # Input is not a valid email, so treat it as a username

        # If user is still None, credentials are invalid
        if user is None:
            return JsonResponse({'error': 'Invalid email or password'}, status=400)

        # Log the user in
        login(request, user)

        # Return a success response or redirect
        return JsonResponse({'success': 'Login successful', 'redirect_url': '/dashboard/'}, status=200)
       

    
