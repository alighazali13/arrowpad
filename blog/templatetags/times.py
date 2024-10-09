from django import template
from arrowpad.functions import getJdatetime_JMonth

register = template.Library()

@register.filter
def jdatetimeFormat(value):

    date = getJdatetime_JMonth(value)

    return date