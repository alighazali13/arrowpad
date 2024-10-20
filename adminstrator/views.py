from django.shortcuts import render, redirect

from arrowpad.functions import getActiveCategories, getCategoryObjectWithEnName
from blog.functions import getBlogObjects
from blog.forms import *

from adminstrator.models import adminLogin


def loginAdmin(request):

    return render(request, 'adminstrator/login.html')

def logoutAdmin(request):
    if 'admin_phoneNumber_s' not in request.session :
        return redirect('loginAdmin')
    else:
        del request.session['admin_phoneNumber_s']
        return redirect('/')


def statistics(request):
    
    if 'admin_phoneNumber_s' not in request.session:
        return redirect('loginAdmin')
    else:
        adminLoginObject = adminLogin.objects.get(phoneNumber = request.session['admin_phoneNumber_s']) 
        ul_on = 'statistics'
        # li_on = ''
        parent_page = 'اروپد'
        this_page = 'آمار'

        cetegoriesObject = getActiveCategories()


        context = {
            'ul_on' : ul_on,
            # 'li_on' : li_on,
            'this_page' : this_page,
            'parent_page' : parent_page,
            'categories' : cetegoriesObject,
            'adminLogin' : adminLoginObject,
        }

        return render(request, 'adminstrator/statistics.html', context)



def blogManagement(request, en_name):
    if 'admin_phoneNumber_s' not in request.session:
        return redirect('loginAdmin')
    else:
        adminLoginObject = adminLogin.objects.get(phoneNumber = request.session['admin_phoneNumber_s']) 
        ul_on = 'blogs'
        li_on = f'{en_name}_managements'
        parent_page = 'اروپد/بلاگ ها'
        this_page = 'مدیریت کیوسک'
        cetegoriesObject = getActiveCategories()
        thiscetegoryObject = getCategoryObjectWithEnName(en_name)

        blogsObjects = getBlogObjects(thiscetegoryObject)

        context = {
            'ul_on' : ul_on,
            'li_on' : li_on,
            'this_page' : this_page,
            'parent_page' : parent_page,
            'categories' : cetegoriesObject,
            'adminLogin' : adminLoginObject,
            'category' : thiscetegoryObject,

            'blogs' : blogsObjects,
            }

        return render(request, 'adminstrator/blogs/blog_managements.html', context)
    
def addBlog(request, en_name):
    if 'admin_phoneNumber_s' not in request.session:
        return redirect('loginAdmin')
    else:
        adminLoginObject = adminLogin.objects.get(phoneNumber = request.session['admin_phoneNumber_s']) 
        ul_on = 'blogs'
        li_on = f'add_{en_name}'
        parent_page = 'اروپد/بلاگ ها'
        this_page = 'اضافه کردن کیوسک جدید'
        cetegoriesObject = getActiveCategories()
        thiscetegoryObject = getCategoryObjectWithEnName(en_name)

        blogForm = blog_form()
        blogMetaForm = blogMeta_form()
        blogSlidesForm = blogSlides_form()
        blogVideoForm = blogVideo_form()


        context = {
            'ul_on' : ul_on,
            'li_on' : li_on,
            'this_page' : this_page,
            'parent_page' : parent_page,
            'categories' : cetegoriesObject,
            'adminLogin' : adminLoginObject,
            'category' : thiscetegoryObject,

            'blogForm' : blogForm,
            'blogMetaForm' : blogMetaForm,
            'blogSlidesForm' : blogSlidesForm,
            'blogVideoForm' : blogVideoForm
            }


        return render(request, 'adminstrator/blogs/add_blog.html', context)



