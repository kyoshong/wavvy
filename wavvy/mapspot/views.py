from django.shortcuts import render


def mapspot(request):
    return render(request, 'spot/mapspot.html')