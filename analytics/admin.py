from django.contrib import admin
from .models import *

class blogAnalytics_admin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'date', 'view', 'analytics_types']
admin.site.register(blogAnalytics, blogAnalytics_admin)