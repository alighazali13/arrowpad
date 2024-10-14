from django.http import JsonResponse
from django.shortcuts import redirect, render
import  random, datetime, json, jdatetime

def account_validation(request):
    status = 500
    data = json.loads(request.POST.get('getdata'))
    phonenumber = data['phonenumber']
    password = data['password']

    # Is there such a number?
    if AdminLogin.objects.filter(phonenumber=phonenumber).exists():
        # Get the admin object that has this phone number
        admin_login = AdminLogin.objects.get(phonenumber=phonenumber)
        # Check password 
        if admin_login.password == password:
            status = 200
            msg = 'ورود شما موفقیت آمیز بود چند لحظه صبر کنید .'
            request.session['admin_login_username'] = admin_login.username
            admin_login.lastlogin = jdatetime.date.today
            admin_login.save()
        else:
            msg = 'رمز عبور یا شماره وارد شده صحیح نمی باشند .'
    else:
        msg = 'رمز عبور یا شماره وارد شده صحیح نمی باشند .'

    context = {
        'status':status,
        'msg':msg,
    }
    
    return JsonResponse(context)