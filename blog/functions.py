from django.db.models import Prefetch

from .models import blog, blogMeta,  blogView, blogViewTypesChoices, blogComment, blogReplies
from arrowpad.models import categories



def getBlogObjects(category):
    return blog.objects.filter(categories=category, active=True).order_by('-id')

def getBlogObjectByUrl(url):

    blogObject = blog.objects.none()
    if blog.objects.filter(url=url, active=True).exists():
        blogObject = blog.objects.get(url=url, active=True)

    return blogObject

def getBlogObjectById(id, categoryObject=None):
    """
    Id can’t be zero or negative 
    and 
    if this id is last blog we'll show first blog for next
    """
    blogObject = blog.objects.none()
    print(id)
    if categoryObject is None:
        if id >= 1:
            if blog.objects.filter(id=id, active=True).exists():
                blogObject = blog.objects.get(id=id, active=True)
            else:
                blogObject = blog.objects.filter(active=True).order_by('id').first()
        else:
            if blog.objects.filter(active=True).exists():
                blogObject = blog.objects.filter(active=True).last()
    else:
        if id >= 1:
            
            if blog.objects.filter(id=id, categories=categoryObject, active=True).exists():
                blogObject = blog.objects.get(id=id, categories=categoryObject, active=True)
            else:
                blogObject = blog.objects.filter(categories=categoryObject, active=True).order_by('id').first()
        else:
            if blog.objects.filter(categories=categoryObject, active=True).exists():
                blogObject = blog.objects.filter(categories=categoryObject, active=True).last()

        
    return blogObject

def getBlogMeta(blogObject):
    
    blogMetaObject = blogMeta.objects.none()
    if blogMeta.objects.filter(blog = blogObject).exists():
        blogMetaObject = blogMeta.objects.get(blog = blogObject)
    return blogMetaObject

def getBlogs(num, types=None, currentBlog = None, categoryObject = None):
    
    blogsObjects = blog.objects.none()
    if categoryObject is None:
        if blog.objects.filter(active=True).exists():
            if types is None:
                if currentBlog is None:
                    blogsObjects = blog.objects.filter(active=True).order_by('-id')[:num]
                else:
                    blogsObjects = blog.objects.filter(active=True).exclude(id=currentBlog.id).order_by('-id')[:num]

            if types == 'popular':
                if currentBlog is None:
                    blogsObjects = blog.objects.filter(active=True).order_by('-totalView')[:num]
                else:
                    blogsObjects = blog.objects.filter(active=True).exclude(id=currentBlog.id).order_by('-totalView')[:num]
    else:
        if blog.objects.filter(active=True, categories=categoryObject).exists():
            if types is None:
                if currentBlog is None:
                    blogsObjects = blog.objects.filter(active=True, categories=categoryObject).order_by('-id')[:num]
                else:
                    blogsObjects = blog.objects.filter(active=True, categories=categoryObject).exclude(id=currentBlog.id).order_by('-id')[:num]

            if types == 'popular':
                if currentBlog is None:
                    blogsObjects = blog.objects.filter(active=True, categories=categoryObject).order_by('-totalView')[:num]
                else:
                    blogsObjects = blog.objects.filter(active=True, categories=categoryObject).exclude(id=currentBlog.id).order_by('-totalView')[:num]

    print(categoryObject)

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




    