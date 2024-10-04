from .models import blog, blogMeta,  blogView, blogViewTypesChoices
from arrowpad.models import categories


def getBlogObjects(category):

    categoryObject = categories.objects.none()
    blogObjects = blog.objects.none()
    if categories.objects.filter(en_name=category['en'], active=True).exists():
        categoryObject = categories.objects.get(en_name=category['en'], active=True)
        if blog.objects.filter(categories=categoryObject, active=True).exists():
            blogObjects = blog.objects.filter(categories=categoryObject, active=True)

    return blogObjects

def getBlogObject(url):

    blogObject = blog.objects.none()
    if blog.objects.filter(url=url, active=True).exists():
        blogObject = blog.objects.get(url=url, active=True)

    return blogObject

def getBlogMeta(blogObject):
    
    blogMetaObject = blogMeta.objects.none()
    if blogMeta.objects.filter(blog = blogObject).exists():
        blogMetaObject = blogMeta.objects.get(blog = blogObject)
    return blogMetaObject

def getBlogs(num, currentBlog):

    
    blogsObjects = blog.objects.none()
    if blog.objects.filter(active=True).exists():
        blogsObjects = blog.objects.filter(active=True).exclude(id=currentBlog.id).order_by('-id')[:num]
    return blogsObjects

def getBlogViewTotal(blogObject):
    
    blogViewObject = blogView.objects.none()
    if blogView.objects.filter(blog = blogObject, types = blogViewTypesChoices.total).exists():
        blogViewObject = blogView.objects.get(blog = blogObject, types = blogViewTypesChoices.total)
    view = blogViewObject.view
    return view

