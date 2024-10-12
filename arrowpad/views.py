from django.shortcuts import render

from .models import categories
from blog.models import blog

def landing_page(request):
    
    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    blogs_by_category = {}
    for category in categoriesObject:
        blogs_by_category[category.en_name] = blog.objects.filter(categories=category).order_by('-publishedAt')[:6]

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject,
        'blogs_by_category' : blogs_by_category
    }

    return render(request, 'arrowpad/index.html', contexts)
