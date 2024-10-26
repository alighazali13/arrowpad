from django.contrib import admin
from .models import *

class blog_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'categories', 'active']
admin.site.register(blog, blog_admin)

class blogTags_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'usageCount', 'url']
admin.site.register(blogTags, blogTags_admin)

class blogMeta_admin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'metaTitle']
admin.site.register(blogMeta, blogMeta_admin)

# class blogSlides_admin(admin.ModelAdmin):
#     list_display = ['id', 'blog']
# admin.site.register(blogSlides, blogSlides_admin)

class blogVideo_admin(admin.ModelAdmin):
    list_display = ['id', 'blog']
admin.site.register(blogVideo, blogVideo_admin)

class blogView_admin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'date', 'view']
admin.site.register(blogView, blogView_admin)

class blogComment_admin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'name', 'email', 'comment', 'active']
admin.site.register(blogComment, blogComment_admin)

class blogReplies_admin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'admin', 'reply', 'active']
admin.site.register(blogReplies, blogReplies_admin)
