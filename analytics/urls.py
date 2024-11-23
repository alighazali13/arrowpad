from django.urls import path
from . import ajaxdef


urlpatterns = [
    path('blogs/manage/getBlogView/', ajaxdef.get_blog_view),
]