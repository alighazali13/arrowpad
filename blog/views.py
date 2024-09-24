from django.shortcuts import render

def kiosk(request):

    return render(request, 'kiosk/kiosk.html')
