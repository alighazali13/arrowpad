from django.urls import path
from . import views, ajaxdef

urlpatterns = [
    path('signin/', views.loginAdmin, name='admin_login'),
    path('logout/', views.logoutAdmin, name='logoutAdmin'),

    path('', views.statistics, name='statistics'),
    path('manage/<str:en_name>', views.blogManagement, name='blog_details'),
    path('add/<str:en_name>', views.addBlog, name='addBlog'),
    path('update/<str:en_name>/<str:url>', views.updateBlog, name='updateBlog'),
    path('statistics/<str:en_name>/<str:url>', views.statisticsBlog, name='statisticsBlog'),
    

    path('signin/valvalidation/', ajaxdef.accountValidation),
    # path('', ajaxdef.)
]