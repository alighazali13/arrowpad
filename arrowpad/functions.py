from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Prefetch
import jdatetime

from blog.models import blog
from .models import categories



def getJdatetime_JMonth(value):

    months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 
          'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    
    year, month, day = map(int, str(value).split('-'))
    myDate = jdatetime.date(year, month, day)

    return f"{myDate.day} {months[myDate.month - 1]} {myDate.year}"

def paginate(objects, perPage, request):

      object_page = Paginator(objects, perPage)
      page_number = request.GET.get('page')
      try:
            result = object_page.get_page(page_number)
      except PageNotAnInteger:
            result = object_page.page(1)
      except EmptyPage:
            result = object_page.page(object_page.num_pages)

      return result

def getCategoriesWithBlogs(categoriesObject, num):
      blogs_by_category = {
        category: blog.objects.filter(categories=category, active=True).order_by('-id')[:6] 
        for category in categoriesObject
      }
      
      return blogs_by_category

def getCategoryObjects(title):

      return categories.objects.get(title=title)
      

      
