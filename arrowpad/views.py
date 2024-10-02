from django.shortcuts import render

from .models import categories

def landing_page(request):
    
    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject
    }

    return render(request, 'arrowpad/index.html', contexts)
