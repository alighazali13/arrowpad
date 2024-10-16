from django.http import JsonResponse
from django.shortcuts import redirect, render
import  random, datetime, json, jdatetime

from blog.models import blog, blogComment

def addComment(request):
    status = 500
    msg = ''
    data = json.loads(request.POST.get('getdata'))
    
    try :
        blogObject = blog.objects.get(url=data['url'])
        blogComment.objects.create(
            blog = blogObject,
            name = data['author'],
            email = data['email'],
            comment = data['comment'],
        )
        status = 200
        msg = f' نظر شما ثبت شد و پس از تایید ادمین برای کاربران قابل مشاهده خواهد شد . '
    except blog.DoesNotExist:
        msg = f' مشکلی پیش آمده است لطفا بعدا تلاش کنید . '
        status = 404
    
    print(msg)
    return JsonResponse({
        'status':status,
        'msg':msg,
    })

