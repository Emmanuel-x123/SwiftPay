from .models import OTPCODE, User
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from  .mailer_otp import send_otp

class Email_verifyView(View):
    def get(self, request):
        return render(request, 'base/otpverify.html')
    

    def post(self, request):
        otp_user = request.POST['otp_code']

        if not otp_user:
            return JsonResponse({'error': 'Verification code is not provided'}, status=400)
        
        try:
            user_otp_records = OTPCODE.objects.get(email_otp=otp_user)
            # the user for otp verification
            user = user_otp_records.user

        except OTPCODE.DoesNotExist:
               return JsonResponse({'error': 'Invalid Verification Code'}, status=400)
        
        if user_otp_records.is_otp_expired():
             send_otp(user.email)
             return JsonResponse({'error': 'OTP code has expired. A new code has ben sent to your email'}, status=400)
        
        if user.email_varified:
             return JsonResponse({'error': 'Email is already verified'}, status=400)
        
        user.email_varified =True
        user.save()
        return JsonResponse({'success': 'Email is verified successfully'}, status=200)