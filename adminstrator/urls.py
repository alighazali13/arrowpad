from django.urls import path
from . import views, ajaxdef

urlpatterns = [
    path('signin/', views.loginAdmin, name='loginAdmin'),
    path('signin/valvalidation/', ajaxdef.accountValidation),
    path('logout/', views.logoutAdmin, name='logoutAdmin'),



    path('', views.statistics, name='statistics'),
    path('manage/<str:en_name>', views.blogManagement, name='blog_details'),
    path('add/<str:en_name>', views.addBlog, name='addBlog'),

]