from django.shortcuts import render

def kiosk(request):

    return render(request, 'kiosk/kiosk.html')

def kiosk_detailes(request, meta_title):

    return render(request, 'kiosk/kiosk_detailes.html')
