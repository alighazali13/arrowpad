
import json
from django.http import JsonResponse
from django.shortcuts import redirect
from .functions import fetch_object_with_monthly_analytics_by_url
from .functions import view_fixer

from adminstrator.models import adminLogin


def get_blog_view(request): 
    
    if 'admin_phoneNumber_s' not in request.session:
        return redirect('loginAdmin')
    else:
        print('hi')
        adminLoginObject = adminLogin.objects.get(phoneNumber = request.session['admin_phoneNumber_s']) 
        data = json.loads(request.POST.get('getdata'))
        print(data['blogUrl'])
        blog_obj = fetch_object_with_monthly_analytics_by_url(data['blogUrl'], 'blog', 12)
        latest_analytics = blog_obj.latest_analytics
        print('latest_analytics')
        print(latest_analytics)
        analytics_res =view_fixer(latest_analytics, 12)
        print(analytics_res)

        return JsonResponse(analytics_res)