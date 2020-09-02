from django.shortcuts import render ,get_object_or_404, HttpResponseRedirect
from .models import ForcastData, Spot
import datetime
from datetime import timedelta
from django.views.generic import DeleteView


def grap(request):
    spot_list = Spot.objects.all()
    context ={'spot_list': spot_list}
    return render(request, 'chart/radar_chart.html',context)

class WeatherDetailView(DeleteView):
    model = Spot
    template_name = 'chart/weather_detail.html' 


def weather_list(request):
    dt = datetime.datetime.now()
    dt1 = dt.strftime("%A %d")

    dt2 = timedelta(days=1)
    dt2 = dt + dt2 
    dt2 = dt2.strftime("%A %d")

    dt3 = timedelta(days=2)
    dt3 = dt + dt3 
    dt3 = dt3.strftime("%A %d")
    
    dt4 = timedelta(days=3)
    dt4 = dt + dt4 
    dt4 = dt4.strftime("%A %d")

    dt5 = timedelta(days=4)
    dt5 = dt + dt5 
    dt5 = dt5.strftime("%A %d")
    
    dt6 = timedelta(days=5)
    dt6 = dt + dt6 
    dt6 = dt6.strftime("%A %d")

    dt7 = timedelta(days=6)
    dt7 = dt + dt7 
    dt7 = dt7.strftime("%A %d")

    time_list = ['00','03','06','09','12','15','18','21']
    weather_data = ForcastData.objects.all()
    
    context = {'dt1' : dt1,
                'dt2' : dt2,
                'dt3' : dt3,
                'dt4' : dt4,
                'dt5' : dt5,
                'dt6' : dt6,
                'dt7' : dt7,
                'weather_data' : weather_data,
                'time_list' : time_list}
    return render(request,'chart/weather_detail.html',context)



def weather(request):
    dt = datetime.datetime.now()
    dt1 = dt.strftime("%A %d")

    dt2 = timedelta(days=1)
    dt2 = dt + dt2 
    dt2 = dt2.strftime("%A %d")

    dt3 = timedelta(days=2)
    dt3 = dt + dt3 
    dt3 = dt3.strftime("%A %d")
    
    dt4 = timedelta(days=3)
    dt4 = dt + dt4 
    dt4 = dt4.strftime("%A %d")

    dt5 = timedelta(days=4)
    dt5 = dt + dt5 
    dt5 = dt5.strftime("%A %d")
    
    dt6 = timedelta(days=5)
    dt6 = dt + dt6 
    dt6 = dt6.strftime("%A %d")

    dt7 = timedelta(days=6)
    dt7 = dt + dt7 
    dt7 = dt7.strftime("%A %d")

    time_list = ['00','03','06','09','12','15','18','21']
    weather_data = ForcastData.objects.all()
    
    context = {'dt1' : dt1,
                'dt2' : dt2,
                'dt3' : dt3,
                'dt4' : dt4,
                'dt5' : dt5,
                'dt6' : dt6,
                'dt7' : dt7,
                'weather_data' : weather_data,
                'time_list' : time_list}
    return render(request,'chart/weather.html',context)

