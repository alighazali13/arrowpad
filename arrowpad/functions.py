import jdatetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def getJdatetime_JMonth(value):

    months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 
          'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    
    year, month, day = map(int, str(value).split('-'))
    myDate = jdatetime.date(year, month, day)
    formatted_date = f"{myDate.day} {months[myDate.month - 1]} {myDate.year}"

    return formatted_date

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