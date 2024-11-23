import json, jdatetime
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import adminLogin, adminInformation, adminCodes
from arrowpad.functions import sendCode, validation


def accountValidation(request):
    context = {}
    data = json.loads(request.POST.get('getdata'))
    print(data['protocol'])
    if data['protocol'] == 'validation' :

        phoneNumber = data['phoneNumber']
        if adminLogin.objects.filter(phoneNumber=phoneNumber).exists():
            status = 200
            code = sendCode(phoneNumber, 'admin')
            print(code)
            print('code1')
            context = {
            'status' : status,
            'phoneNumber' : phoneNumber,
            }
        else:
            status = 404
            context = {
                'status' : status,
                'msg' : 'حساب کاربری با این شماره پیدا نشد.'
            }
    if data['protocol'] == 'code' :
        inputCode = data['code']
        phoneNumber = data['phoneNumber']
        print('phoneNumber')
        print(phoneNumber)
        print('inputCode')
        print(inputCode)
        if validation(inputCode, phoneNumber, 'admin') == True :
            adminLoginObject = adminLogin.objects.get(phoneNumber=phoneNumber)
            request.session['admin_phoneNumber_s'] = adminLoginObject.phoneNumber
            adminLoginObject.lastLogin = jdatetime.date.today()
            adminLoginObject.save()
            status = 200
            url = '/a/d/min/strator/'
            context = {
                'status' : status,
                'url' : url
            }
            print(context)
            
        else:
            status = 500
            context = {
                'status' : status,
                'msg' : 'کد وارد شده اشتباه می باشد.'
            }


    return JsonResponse(context)


