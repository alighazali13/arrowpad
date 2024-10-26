from django.shortcuts import render, redirect
from django.urls import reverse

from arrowpad.functions import getActiveCategories, getCategoryObjectWithEnName, insertTags, updateBlogTags, isValueChanged
from blog.functions import getBlogObjects, getBlogObjectByUrl, getBlogMeta, getblogVideo
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
        # blogSlidesForm = blogSlides_form()
        blogVideoForm = blogVideo_form()

        if request.POST:
            if 'addBlog_BTN' in request.POST:
                title = request.POST.get('title', 'null')
                url = request.POST.get('url', 'null')
                category = request.POST.get('category', 'null')
                urlVideo = request.POST.get('urlVideo', 'null')
                brief = request.POST.get('brief', 'null')
                content = request.POST.get('content', 'null')
                # sliderImages = request.FILES.getlist('sliderImages', [])
                poster = request.FILES.get('poster', None)  
                metaTitle = request.POST.get('metaTitle', 'null')
                metaTags = request.POST.get('metaTags', 'null')
                metaKeywords = request.POST.get('metaKeywords', 'null')
                metaDescription = request.POST.get('metaDescription', 'null')
                
                                    
                if content != 'null' and poster is not None:  
                    hasVideo = urlVideo != 'null'
                    # hasSlider = bool(sliderImages)  
                    tagsList = metaTags.split('-') if metaTags and metaTags != 'null' else []

                    insertTags(tagsList, 'blog')
                    categoryObject = categories.objects.get(id=category)

                    blogObject = blog.objects.create(
                        author=adminLoginObject.adminInformation,
                        title=title,
                        poster=poster,
                        posterWebp=poster,
                        posterJpeg=poster,
                        categories=categoryObject,
                        brief=brief,
                        content=content,
                        url=url,
                        hasVideo=hasVideo,
                        # hasSlider=hasSlider,
                        isUpdated=False,
                    )
                    categoryObject.postCount += 1
                    categoryObject.save()

                    
                    blogMeta.objects.create(
                        blog=blogObject,
                        metaTitle=metaTitle,
                        metaTags=metaTags,
                        metaDescription=metaDescription,
                        metaKeywords=metaKeywords
                    )
                    blogView.objects.create(
                        blog=blogObject,
                        view=0
                    )
                    if hasVideo:
                        blogVideo.objects.create(
                            blog=blogObject,
                            urlVideo=urlVideo
                        )
                    # if hasSlider:
                    #     for image in sliderImages:
                    #         blogSlides.objects.create(
                    #             blog=blogObject,
                    #             image=image,
                    #             imageWebp=image
                    #         )
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
            # 'blogSlidesForm' : blogSlidesForm,
            'blogVideoForm' : blogVideoForm
            }


        return render(request, 'adminstrator/blogs/add_blog.html', context)

def updateBlog(request, en_name, url):
    if 'admin_phoneNumber_s' not in request.session:
        return redirect('loginAdmin')
    else:
        adminLoginObject = adminLogin.objects.get(phoneNumber = request.session['admin_phoneNumber_s']) 
        
        blogObject = getBlogObjectByUrl(url)
        blogMetaObject = blogObject.blogMeta
        blogVideoObject = blogObject.blogVideo
        
        ul_on = 'blogs'
        li_on = f'update_{en_name}'
        parent_page = 'اروپد/بلاگ ها'
        this_page = f'بروزرسانی {en_name} به نام {blogObject.title} '
        cetegoriesObject = getActiveCategories()
        thiscetegoryObject = getCategoryObjectWithEnName(en_name)

        thiscetegoryObject = getCategoryObjectWithEnName(blogObject.categories.en_name)

        blogForm = blog_form(instance=blogObject)
        blogMetaForm = blogMeta_form(instance=blogMetaObject)
        # blogSlidesForm = blogSlides_form(instance=getBlogSlides(blogObject))
        blogVideoForm = blogVideo_form(instance=blogVideoObject)

        if request.POST:
            if 'updateBlog_BTN' in request.POST:
                title = request.POST.get('title', None)
                url = request.POST.get('url', None)
                category_id = request.POST.get('category', None)
                urlVideo = request.POST.get('urlVideo', None)
                brief = request.POST.get('brief', None)
                content = request.POST.get('content', None)
                poster = request.FILES.get('poster', None)
                metaTitle = request.POST.get('metaTitle', None)
                metaTags = request.POST.get('metaTags', None)
                metaKeywords = request.POST.get('metaKeywords', None)
                metaDescription = request.POST.get('metaDescription', None)
                print('category_id')
                print(category_id)
                
                
                # Update blog fields
                updated = False
                if isValueChanged(blogObject.title, title):
                    blogObject.title = title
                    updated = True
                if isValueChanged(blogObject.url, url):
                    blogObject.url = url
                    updated = True
                    urlChanged = True
                if category_id is not None :
                    category = categories.objects.filter(id=category_id).first()
                    if isValueChanged(blogObject.categories, category):
                        blogObject.categories = category
                        updated = True
                if isValueChanged(blogObject.brief, brief):
                    blogObject.brief = brief
                    updated = True
                if isValueChanged(blogObject.content, content):
                    blogObject.content = content
                    updated = True
                if poster and isValueChanged(blogObject.poster, poster):
                    blogObject.poster = poster
                    updated = True
                
                if updated:
                    blogObject.save()
                
                # Update blogMeta fields
                updated_meta = False
                if isValueChanged(blogMetaObject.metaTitle, metaTitle):
                    blogMetaObject.metaTitle = metaTitle
                    updated_meta = True
                if isValueChanged(blogMetaObject.metaTags, metaTags):
                    newTagsList = metaTags.split('-') if metaTags and metaTags != 'null' else []
                    existingTagsList = blogMetaObject.metaTags
                    updateBlogTags(newTagsList, existingTagsList, 'blog')
                    blogMetaObject.metaTags = metaTags
                    updated_meta = True
                if isValueChanged(blogMetaObject.metaDescription, metaDescription):
                    blogMetaObject.metaDescription = metaDescription
                    updated_meta = True
                if isValueChanged(blogMetaObject.metaKeywords, metaKeywords):
                    blogMetaObject.metaKeywords = metaKeywords
                    updated_meta = True

                if updated_meta:
                    blogMetaObject.save()

                # Update blogVideo field
                if isValueChanged(blogVideoObject.urlVideo, urlVideo):
                    blogVideoObject.urlVideo = urlVideo
                    blogVideoObject.save()

            en_name = blogObject.categories.en_name
            return redirect(reverse('blog_details', kwargs={'en_name': en_name}))


        context = {
                'ul_on' : ul_on,
                'li_on' : li_on,
                'this_page' : this_page,
                'parent_page' : parent_page,
                'categories' : cetegoriesObject,
                'adminLogin' : adminLoginObject,
                'category' : thiscetegoryObject,
                'blog' : blogObject,

                'blogForm' : blogForm,
                'blogMetaForm' : blogMetaForm,
                # 'blogSlidesForm' : blogSlidesForm,
                'blogVideoForm' : blogVideoForm,

                }


        return render(request, 'adminstrator/blogs/update_blog.html', context)




