from django.shortcuts import render

from arrowpad.functions import getCategoriesWithBlogs, getActiveBanners

from .models import categories
from blog.models import blog

def landing_page(request):
    
    categoriesStatus = 404

    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        blogs_by_category = getCategoriesWithBlogs(categoriesObject, 6)
        categoriesStatus = 200

    bannersObjects = getActiveBanners()

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'blogs_by_category' : blogs_by_category,

        'banners' : bannersObjects,
    }

    return render(request, 'arrowpad/index.html', contexts)
