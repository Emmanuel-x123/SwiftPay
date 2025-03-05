from django.shortcuts import render

# Create your views here.
# def homePage(request):
#     return render(request, 'base/index.html')

def signUp(request):
    #    username = request.POST['username']
    #    email  = request.POST['email']
    #    phone_no = request.POST['phone']
    #    password = request.POST['password']
    #    password2 = request.POST['password2']




       return render(request, 'base/signup.html')



def loginView(request):
    return render(request, 'base/login.html')

def verifyOtp(request):
    return render(request, 'base/otpverify.html')