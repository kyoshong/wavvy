from django.shortcuts import render
from commu.models import Post


# Create your views here.
def index(request):
    posts= Post.objects.order_by('-pub_date')
    return render(request, 'allpage/index.html',{'posts':posts})
