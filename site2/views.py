from django.shortcuts import render
from .models import mymodel
from .Getmessage import get_title

# Create your views here.
def show(request):
    movies=get_title()

    if mymodel.objects.count()==0:
        for each in movies:
            addition=mymodel(title=each['title'],actor=each['actor'])
            addition.save()

    data=mymodel.objects
    return render(request,'mysite.html',{'data':data})
