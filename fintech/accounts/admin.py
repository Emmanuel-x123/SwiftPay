from django.contrib import admin
from .models import User, PersonalAccount, BusinessAccount, OTPCODE,TwoFactorModel

# Register your models here.
@admin.register(User)
class adminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_superuser', 'email_varified']

@admin.register(TwoFactorModel)
class adminTwoFactorModel(admin.ModelAdmin):
    list_display = ['user', 'is_twofactor_enabled', 'twoFaCode', 'twoFa_created', 'twoFaBackUp', 'is_email_enabled', 'email_otp', 'email_created', 'date_created', 'updated_at']    

@admin.register(PersonalAccount)
class PersonalAccountadmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth','image']


@admin.register(BusinessAccount)
class BusinessAccountAdminr(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'company_name', 'registration_number', 'business_address', 'legal_name']
    
        
@admin.register(OTPCODE)
class OTPcodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_otp', 'phone_otp', 'created_at']
