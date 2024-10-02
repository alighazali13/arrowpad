from django.contrib import admin
from .models import *

class blog_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'categories', 'active']
admin.site.register(blog, blog_admin)

class blogMeta_admin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'metaTitle']
admin.site.register(blogMeta, blogMeta_admin)

class blogSlides_admin(admin.ModelAdmin):
    list_display = ['id', 'blog']
admin.site.register(blogSlides, blogSlides_admin)

class blogVideos_admin(admin.ModelAdmin):
    list_display = ['id', 'blog']
admin.site.register(blogVideos, blogVideos_admin)
