from django.contrib import admin
from .models import *

class categories_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'active']
admin.site.register(categories, categories_admin)

class categoryMeta_admin(admin.ModelAdmin):
    list_display = ['id', 'category', 'metaTitle']
admin.site.register(categoryMeta, categoryMeta_admin)


class banner_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
admin.site.register(banner, banner_admin)
