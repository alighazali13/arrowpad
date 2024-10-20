from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Prefetch
import jdatetime, random

from blog.models import blog
from .models import categories, categoryMeta
from adminstrator.models import adminCodes



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

def getActiveCategories():
     try:
          return categories.objects.filter(active=True)
     except categories.DoesNotExist:
          return None

def getCategoriesWithBlogs(categoriesObject, num):
      blogs_by_category = {
        category: blog.objects.filter(categories=category, active=True).order_by('-id')[:6] 
        for category in categoriesObject
      }
      
      return blogs_by_category

def getCategoryObjectWithTitle(title):
      try : 
            return categories.objects.get(title=title)
      except categories.DoesNotExist:
            return None

def getCategoryObjectWithEnName(en_name):
      try : 
            return categories.objects.get(en_name=en_name)
      except categories.DoesNotExist:
            return None

def getCategoryMetaObject(categoryObject):
      try : 
            return categoryMeta.objects.get(category=categoryObject)
      except categoryMeta.DoesNotExist:
            return None



def sendCode(phoneNumber, client):
    if client == 'admin':
      code = random.randint(10000,99999)
      adminCodes.objects.create(
      phoneNumber = phoneNumber,
      code = code
      )
    return code

def validation(inputCode, phoneNumber, reqType):
    print(inputCode)
    print(phoneNumber)
    if reqType == 'admin':
        if adminCodes.objects.filter(phoneNumber=phoneNumber, code=inputCode).exists():
            status = True
            adminCodes.objects.get(phoneNumber=phoneNumber, code=inputCode).delete()
        else:
            status = False
    return status

def reset_code_sent():
    adminCodes.objects.all().delete()
