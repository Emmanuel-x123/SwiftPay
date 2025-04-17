import base64
from io import BytesIO
from django.shortcuts import render
from django.views import View
import pyotp
import qrcode
from .models import TwoFactorModel
from django.contrib.auth.mixins import LoginRequiredMixin








class SetUpTwoFa(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        login_user = request.user
        user_twofa = TwoFactorModel.objects.get_or_create(user=login_user)[0]
        user_twofa.generate_twofactor_secret()

        twoFa_url = pyotp.totp.TOTP(user_twofa.twoFaCode).provisioning_uri(
            name = request.user.username,
            issuer_name= 'SwiftPay'
        )

        qr = qrcode.QRCode(
           version=1,
           box_size=10,
           border=4 
        )
        qr.add_data(twoFa_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        qr_code_decode = base64.b64encode(buffer.getvalue()).decode()

        return render(request, 'twoFactor/set2fa.html', {'twofa_secret': user_twofa.twoFaCode, 'qr_code_decode': qr_code_decode})