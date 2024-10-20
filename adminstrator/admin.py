from django.contrib import admin
from .models import *

class adminInformation_admin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'displayName', 'email', 'birthday_date']
admin.site.register(adminInformation, adminInformation_admin)

class adminLogin_admin(admin.ModelAdmin):
    list_display = ['id', 'adminInformation', 'password', 'phoneNumber', 'joinedAt', 'updatedAt', 'lastLogin']
admin.site.register(adminLogin, adminLogin_admin)


class adminCodes_admin(admin.ModelAdmin):
    list_display = ['id', 'phoneNumber', 'code']
admin.site.register(adminCodes, adminCodes_admin)
