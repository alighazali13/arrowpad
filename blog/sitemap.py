from django.contrib.sitemaps import Sitemap
from .models import blog


class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'
    def items(self):
        return blog.objects.filter(active=True)
    
    def last_mod(self, obj):
        return obj.updatedAt

    def location(self,obj):
        cat_url = str(obj.categories.url)
        blog_url = str(obj.url)
        return '/' + cat_url + blog_url