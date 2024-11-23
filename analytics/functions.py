
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
import json

from blog.models import blog
from analytics.models import blogAnalytics
from analytics.models import blogTypesChoices


def fetch_object_with_monthly_analytics_by_url(url, object_type, numb=None):
    if numb is not None:
        if object_type == 'blog':
            return get_object_or_404(
                blog.objects.prefetch_related(
                    Prefetch('blogAnalytics', 
                        queryset=blogAnalytics.objects.filter(analytics_types=blogTypesChoices.MONTHLY)
                        .order_by('-date')[:numb], 
                        to_attr='latest_analytics')
                    ),
                    url=url,
                )
            

def view_fixer(latest_analytics, numb=None):
    views = []
    if numb is not None:
        for analytics in latest_analytics:
            views.append(analytics.view)
        
        # اگر تعداد روز خرید ها و ویو ها کمتر از 12 باشد در رابط کاربری مشکل بصری پیش می اید
        more_value_need = numb - len(views)
        if more_value_need != 0:
            for i in range(more_value_need):
                views.append(0)

        return({
            'views' : views, 
        })
        


    