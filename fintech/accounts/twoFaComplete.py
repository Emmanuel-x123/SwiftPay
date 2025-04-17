from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import JsonResponse
import pyotp
from .models import TwoFactorModel
from django.contrib.auth.mixins import LoginRequiredMixin


class SetupComplete(LoginRequiredMixin,View):
    login_url = 'login'
    def post(self, request):
        login_user = request.user
        user_twofa = TwoFactorModel.objects.get_or_create(user=login_user)[0]
        twoFacodes = user_twofa.twoFaCode

        if not twoFacodes:
            return JsonResponse({"error": "TOTP Secret not found"},status=404)

        
        otp_token = request.POST.get('otp_token')
        totp_code = pyotp.TOTP(twoFacodes)
        if totp_code.verify(otp_token):
            user_twofa.is_twofactor_enabled = True
            user_twofa.save()
            return JsonResponse({"success": "2FA setup complete"},status=200)
        else:
            return JsonResponse({"error": "Invalid 2FA TOKEN"},status=400)