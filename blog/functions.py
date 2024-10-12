from django.db.models import Prefetch

from .models import blog, blogMeta,  blogView, blogViewTypesChoices, blogComment, blogReplies
from arrowpad.models import categories



def getBlogObjects(category):

    categoryObject = categories.objects.none()
    blogObjects = blog.objects.none()
    if categories.objects.filter(en_name=category['en'], active=True).exists():
        categoryObject = categories.objects.get(en_name=category['en'], active=True)
        if blog.objects.filter(categories=categoryObject, active=True).exists():
            blogObjects = blog.objects.filter(categories=categoryObject, active=True)

    return blogObjects

def getBlogObjectByUrl(url):

    blogObject = blog.objects.none()
    if blog.objects.filter(url=url, active=True).exists():
        blogObject = blog.objects.get(url=url, active=True)

    return blogObject

def getBlogObjectById(id):
    """
    Id can’t be zero or negative 
    and 
    if this id is last blog we'll show first blog for next
    """
    blogObject = blog.objects.none()
    print(id)
    if id >= 1:
        
        # try:
        if blog.objects.filter(id=id, active=True).exists():
            blogObject = blog.objects.get(id=id, active=True)
        else:
            blogObject = blog.objects.filter(active=True).order_by('id').first()
        # except blog.DoesNotExist:
        #     print('exepct')
        #     if blog.objects.filter(active=True).exists():
        #         blogObject = blog.objects.filter(active=True).order_by('id').first()
    else:
        if blog.objects.filter(active=True).exists():
            blogObject = blog.objects.filter(active=True).last()
        
    return blogObject

def getBlogMeta(blogObject):
    
    blogMetaObject = blogMeta.objects.none()
    if blogMeta.objects.filter(blog = blogObject).exists():
        blogMetaObject = blogMeta.objects.get(blog = blogObject)
    return blogMetaObject

def getBlogs(num, types=None, currentBlog = None):
    print(currentBlog)
    
    blogsObjects = blog.objects.none()
    if blog.objects.filter(active=True).exists():
        if types is None:
            if currentBlog is not None:
                blogsObjects = blog.objects.filter(active=True).exclude(id=currentBlog.id).order_by('-id')[:num]
            else:
                blogsObjects = blog.objects.filter(active=True).order_by('-id')[:num]
        if types == 'popular':
            if currentBlog is not None:
                blogsObjects = blog.objects.filter(active=True).exclude(id=currentBlog.id).order_by('-totalView')[:num]
            else:
                blogsObjects = blog.objects.filter(active=True).order_by('-totalView')[:num]

    return blogsObjects

def getBlogViewTotal(blogObject):
    
    blogViewObject = blogView.objects.none()
    if blogView.objects.filter(blog = blogObject, types = blogViewTypesChoices.total).exists():
        blogViewObject = blogView.objects.get(blog = blogObject, types = blogViewTypesChoices.total)
    view = blogViewObject.view
    return view

def getBlogCommentsWithReplies(blogObject):

    blogCommentsObject = blogComment.objects.none()
    if blogComment.objects.filter(blog = blogObject, active=True).exists():
        blogCommentsObject = blogComment.objects.filter(blog=blogObject, active=True).prefetch_related(
            Prefetch(
                'commentReplies', queryset=blogReplies.objects.filter(active=True)
            )
    )

    return blogCommentsObject