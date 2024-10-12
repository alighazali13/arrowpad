from django import template

from blog.models import blog, blogVideos

register = template.Library()

@register.filter
def getVideoUrl(blogObject):
    
    blogVideoObject = blogVideos.objects.filter(blog=blogObject).first()
    
    return blogVideoObject.url if blogVideoObject else None


