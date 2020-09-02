from django.db import models
from django.conf import settings

class Spot(models.Model):
    spot_name = models.CharField(max_length = 100)                 #초당 미터 바람속도
    lat = models.FloatField(max_length = 100)
    lng = models.FloatField(max_length = 100)
    favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favourite')

    def count_likes_user(self): # total likes_user
        return self.favourite.count()

    def __str__(self):
        return self.spot_name

class ForcastData(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, null=True, related_name='spot') # 관계 설정

    airTemperature = models.FloatField()           #섭씨 온도 
    waterTemperature =  models.FloatField()        #물 섭씨 온도
    precipitation = models.FloatField()            #kg / m²의 평균 강수량
        
    waveDirection = models.FloatField()            #파도 방향
    waveHeight = models.FloatField()               #파도 높이
    wavePeriod = models.FloatField()                #파도 주기
        
    windDirection = models.FloatField()            #바람 방향
    gust = models.FloatField()                     #초당 미터 바람속도

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'forecasts'

        
'''
class Forecast(models.Model):
        


    def _str_(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'forecasts'



class ForcastData(models.Model):
    airTemperature =   models.DecimalField(max_digits=10, decimal_places=6)         #섭씨 온도 
    waterTemperature =          #물 섭씨 온도
    precipitation =             #kg / m²의 평균 강수량
        
    waveDirection =             #파도 방향
    waveHeight =                #파도 높이
    wavePeriod =                #파도 주기
        
    windDirection =             #바람 방향
    gust =                      #초당 미터 바람속도

'''