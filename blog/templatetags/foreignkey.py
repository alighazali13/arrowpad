from django import template

from blog.models import blog, blogVideo

register = template.Library()

@register.filter
def getVideoUrl(blogObject):
    
    blogVideoObject = blogVideo.objects.filter(blog=blogObject).first()
    return blogVideoObject.urlVideo if blogVideoObject else None


