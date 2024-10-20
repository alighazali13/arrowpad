from django.shortcuts import render

from .functions import getBlogObjects, getBlogObjectByUrl, getBlogObjectById, getBlogMeta, getBlogs, getBlogCommentsWithReplies
from arrowpad.functions import paginate, getCategoryObjectWithTitle, getCategoryMetaObject, getActiveCategories

from arrowpad.models import categories
from .models import blog, blogTags


def kiosk(request):
    category = {'en' : 'kiosk', 'fa' : 'کیوسک'}


    categoriesObject = getActiveCategories()
    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])
    thisCategoryMetaObjects = getCategoryMetaObject(thisCategoryObjects)

    blogObjects = getBlogObjects(thisCategoryObjects)
    newBlogsObjects = getBlogs(3, 'popular', None, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categories' : categoriesObject,
        'category':thisCategoryObjects,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
        'categoryMeta' : thisCategoryMetaObjects,
    }

    return render(request, 'arrowpad/blog/kiosk/kiosk.html', contexts)

def kiosk_detailes(request, url):
    category = {'en' : 'kiosk', 'fa' : 'کیوسک'}

    categoriesObject = getActiveCategories()

    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])


    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)

    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
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
    category = {'en' : 'souls', 'fa' : 'سولز شناسی'}

    categoriesObject = getActiveCategories()
    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])
    thisCategoryMetaObjects = getCategoryMetaObject(thisCategoryObjects)

    blogObjects = getBlogObjects(thisCategoryObjects)
    newBlogsObjects = getBlogs(3, 'popular', None, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categories' : categoriesObject,
        'category':thisCategoryObjects,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
        'categoryMeta' : thisCategoryMetaObjects,
    }

    return render(request, 'arrowpad/blog/souls/souls.html', contexts)

def souls_detailes(request, url):
    category = {'en' : 'souls', 'fa' : 'سولز شناسی'}

    categoriesObject = getActiveCategories()
    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])

    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)

    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
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
    category = {'en' : 'fact', 'fa' : 'فکت'}

    categoriesObject = getActiveCategories()
    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])
    thisCategoryMetaObjects = getCategoryMetaObject(thisCategoryObjects)

    blogObjects = getBlogObjects(thisCategoryObjects)
    newBlogsObjects = getBlogs(3, 'popular', None, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categories' : categoriesObject,
        'category':thisCategoryObjects,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
        'categoryMeta' : thisCategoryMetaObjects,
    }

    return render(request, 'arrowpad/blog/fact/fact.html', contexts)

def fact_detailes(request, url):
    category = {'en' : 'fact', 'fa' : 'فکت'}

    categoriesObject = getActiveCategories()
    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])

    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)

    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
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
    category = {'en' : 'microscope', 'fa' : 'میکروسکوپ'}

    categoriesObject = getActiveCategories()
    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])
    thisCategoryMetaObjects = getCategoryMetaObject(thisCategoryObjects)

    blogObjects = getBlogObjects(thisCategoryObjects)
    newBlogsObjects = getBlogs(3, 'popular', None, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    paginatedBlogObject = paginate(blogObjects, 5, request )

    contexts = {
        'categories' : categoriesObject,
        'category':thisCategoryObjects,
        'blogs' : paginatedBlogObject,
        'newBlogs' : newBlogsObjects,
        'popularTags' : popularTags,
        'categoryMeta' : thisCategoryMetaObjects,
    }

    return render(request, 'arrowpad/blog/microscope/microscope.html', contexts)

def microscope_detailes(request, url):
    category = {'en' : 'microscope', 'fa' : 'میکروسکوپ'}

    categoriesObject = getActiveCategories()
    thisCategoryObjects = getCategoryObjectWithTitle(category['fa'])

    blogObject = getBlogObjectByUrl(url)
    blogMetaObject = getBlogMeta(blogObject)


    pervBlog = getBlogObjectById(blogObject.id - 1, thisCategoryObjects)
    nextBlog = getBlogObjectById(blogObject.id + 1, thisCategoryObjects)

    blogsObjects = getBlogs(3, 'popular', blogObject, thisCategoryObjects)

    popularTags = blogTags.getPopularTags(limit=10)

    blogCommentObject = getBlogCommentsWithReplies(blogObject)

    contexts = {
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
