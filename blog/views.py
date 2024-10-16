from django.shortcuts import render

from .functions import getBlogObjects, getBlogObjectByUrl, getBlogObjectById, getBlogMeta, getBlogs, getBlogCommentsWithReplies
from arrowpad.functions import paginate, getCategoryObjects

from arrowpad.models import categories
from .models import blog, blogTags


def kiosk(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    
    category = {'en' : 'kiosk', 'fa' : 'کیوسک'}

    blogObjects = getBlogObjects(category)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    newBlogsObjects = getBlogs(3, 'popular', thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
    }

    return render(request, 'arrowpad/blog/kiosk/kiosk.html', contexts)

def kiosk_detailes(request, url):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    category = {'en' : 'kiosk', 'fa' : 'کیوسک'}

    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category' : category,
        'blog' : blogObject,
        'blogMeta' : blogMetaObject,
        'blogsObjects' : blogsObjects,
        'popularTags' : popularTags,
        'pervBlog' : pervBlog,
        'nextBlog' : nextBlog,
        'comments' : blogCommentObject,
    }

    return render(request, 'arrowpad/blog/kiosk/kiosk_detailes.html', contexts)

def souls(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    
    category = {'en' : 'souls', 'fa' : 'سولز شناسی'}
    
    blogObjects = getBlogObjects(category)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    newBlogsObjects = getBlogs(3, 'popular', thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
    }

    return render(request, 'arrowpad/blog/souls/souls.html', contexts)

def souls_detailes(request, url):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    category = {'en' : 'souls', 'fa' : 'سولز شناسی'}

    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category' : category,
        'blog' : blogObject,
        'blogMeta' : blogMetaObject,
        'blogsObjects' : blogsObjects,
        'popularTags' : popularTags,
        'pervBlog' : pervBlog,
        'nextBlog' : nextBlog,
        'comments' : blogCommentObject,
    }

    return render(request, 'arrowpad/blog/souls/souls_detailes.html', contexts)

def fact(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200


    category = {'en' : 'fact', 'fa' : 'فکت'}
    
    blogObjects = getBlogObjects(category)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    newBlogsObjects = getBlogs(3, 'popular', thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
    }

    return render(request, 'arrowpad/blog/fact/fact.html', contexts)

def fact_detailes(request, url):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    category = {'en' : 'fact', 'fa' : 'فکت'}

    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category' : category,
        'blog' : blogObject,
        'blogMeta' : blogMetaObject,
        'blogsObjects' : blogsObjects,
        'popularTags' : popularTags,
        'pervBlog' : pervBlog,
        'nextBlog' : nextBlog,
        'comments' : blogCommentObject,
    }

    return render(request, 'arrowpad/blog/fact/fact_detailes.html', contexts)

def microscope(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    category = {'en' : 'microscope', 'fa' : 'میکروسکوپ'}
    
    blogObjects = getBlogObjects(category)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    newBlogsObjects = getBlogs(3, 'popular', thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category':category,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
    }

    return render(request, 'arrowpad/blog/microscope/microscope.html', contexts)

def microscope_detailes(request, url):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    category = {'en' : 'microscope', 'fa' : 'میکروسکوپ'}

    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)

    thisCategoryObjects = getCategoryObjects(category['fa'])

    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'category' : category,
        'blog' : blogObject,
        'blogMeta' : blogMetaObject,
        'blogsObjects' : blogsObjects,
        'popularTags' : popularTags,
        'pervBlog' : pervBlog,
        'nextBlog' : nextBlog,
        'comments' : blogCommentObject,
    }

    return render(request, 'arrowpad/blog/microscope/microscope_detailes.html', contexts)
