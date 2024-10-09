from django.shortcuts import render
from .functions import getBlogObjects, getBlogObject, getBlogMeta, getBlogs

from arrowpad.models import categories
from .models import blog, blogTags


def kiosk(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    
    category = {'en' : 'kiosk', 'fa' : 'کیوسک'}
    print(category['en'])
    blogObjects = getBlogObjects(category)

    newBlogsObjects = getBlogs(3, 'popular')

    popularTags = blogTags.getPopularTags(limit=10)


    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : blogObjects,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,

    }

    return render(request, 'kiosk/kiosk.html', contexts)

def kiosk_detailes(request, url):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    blogObject = getBlogObject(url)
    blogMetaObject = getBlogMeta(blogObject)

    blogsObjects = getBlogs(3, 'popular', blogObject)

    popularTags = blogTags.getPopularTags(limit=10)
    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'blog' : blogObject,
        'blogMeta' : blogMetaObject,
        'blogsObjects' : blogsObjects,
        'popularTags' : popularTags,
    }

    return render(request, 'kiosk/kiosk_detailes.html', contexts)

def souls(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    
    category = {'en' : 'souls', 'fa' : 'سولز شناسی'}
    print(category['en'])
    blogObjects = getBlogObjects(category)

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : blogObjects
    }

    return render(request, 'souls/souls.html', contexts)

def souls_detailes(request, meta_title):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject
    }

    return render(request, 'souls/souls_detailes.html', contexts)

def fact(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200


    category = {'en' : 'fact', 'fa' : 'فکت'}
    print(category['en'])
    blogObjects = getBlogObjects(category)

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : blogObjects
    }

    return render(request, 'fact/fact.html', contexts)

def fact_detailes(request, meta_title):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject
    }

    return render(request, 'fact/fact_detailes.html', contexts)

def microscope(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    category = {'en' : 'microscope', 'fa' : 'میکروسکوپ'}
    print(category['en'])
    blogObjects = getBlogObjects(category)

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : blogObjects
    }

    return render(request, 'microscope/microscope.html', contexts)

def microscope_detailes(request, meta_title):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject
    }

    return render(request, 'microscope/microscope_detailes.html', contexts)
