from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import pyotp
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login
from .models import TwoFactorModel





class VerifyTwoFaToken(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        return render(request, 'twoFactor/complete.html')
    
    def post(self, request):
        twfa_token = request.POST.get('otp_token')
        user = request.user

        if not twfa_token:
            return JsonResponse({"error": "2FA field cannot be empty"},status=401)

        if not user.is_authenticated:
            return JsonResponse({"error": "user is not authenticated"},status=401)
        

        userTwoFa = TwoFactorModel.objects.get(user=user)
        pyot_secret = userTwoFa.twoFaCode

        if not pyot_secret:
            return JsonResponse({"error": "2FA not found"},status=401)
        

        secret_2fa = pyotp.TOTP(pyot_secret)
        if secret_2fa.verify(twfa_token):
            login(request, user)
            return JsonResponse({'success': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': '2FA token is invalid'}, status=401)
