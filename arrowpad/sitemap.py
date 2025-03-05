from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class LandingPageSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = 'https'
    def items(self):
        return ['landing_page']
    
    def location(self, item):
            return reverse(item)
    
