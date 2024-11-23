# PEP8 (Python Enhancement Proposals)
from django.db import models
from django_jalali.db import models as jmodels
import jdatetime

from blog.models import blog

class blogTypesChoices(models.IntegerChoices):
    NULL = 0, 'No Type'
    DAILY = 1, 'daily'
    MONTHLY = 2, 'monthly'

class blogAnalytics(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogAnalytics')
    date = jmodels.jDateField(default=jdatetime.date.today)
    analytics_types = models.IntegerField(default = blogTypesChoices.NULL, choices=blogTypesChoices.choices)
    view = models.IntegerField(default=0)