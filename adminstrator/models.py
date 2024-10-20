from django.db import models
from django.utils.translation import gettext as _
import uuid, os, jdatetime, re
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField


class adminInformation(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=70)
    displayName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    birthday_date = jmodels.jDateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.firstName + self.lastName

class adminLogin(models.Model):
    adminInformation = models.ForeignKey(adminInformation, on_delete=models.CASCADE, related_name='adminLogin')
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=13)
    joinedAt = jmodels.jDateTimeField(default=jdatetime.datetime.now)
    updatedAt = jmodels.jDateTimeField(default=jdatetime.datetime.now)
    lastLogin = jmodels.jDateTimeField(default=jdatetime.datetime.now)

    def __str__(self) -> str:
        return self.adminInformation.firstName + ' ' + self.adminInformation.lastName

class adminCodes(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    phoneNumber = models.CharField(max_length=12, unique=True)
    code = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.adminLogin.adminInformation.firstName + self.adminLogin.adminInformation.lastName