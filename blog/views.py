from django.shortcuts import render

from arrowpad.models import categories

def kiosk(request):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject
    }

    return render(request, 'kiosk/kiosk.html', contexts)

def kiosk_detailes(request, meta_title):

    categoriesStatus = 404
    categoriesObject = categories.objects.none()
    if categories.objects.filter(active=True).exists():
        categoriesObject = categories.objects.filter(active=True)
        categoriesStatus = 200

    

    contexts = {
        'categoriesStatus' : categoriesStatus,
        'categories' : categoriesObject
    }

    return render(request, 'kiosk/kiosk_detailes.html', contexts)
