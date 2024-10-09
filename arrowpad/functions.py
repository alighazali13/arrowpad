import jdatetime


def getJdatetime_JMonth(value):

    months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 
          'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    
    year, month, day = map(int, str(value).split('-'))
    myDate = jdatetime.date(year, month, day)
    formatted_date = f"{myDate.day} {months[myDate.month - 1]} {myDate.year}"

    return formatted_date