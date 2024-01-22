from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Tips
# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 =Tips.objects.all()
    return render(request, "index.html",{'result':obj,'result2':obj1})
# def addition(request):
#     num1 = request.GET['num1']
#     num2 = request.GET['num2']
#     res = int(num1)+int(num2)
#     return render(request,"result.html",{'result':res})
# def contact(request):
#     return HttpResponse("Hello iam Contact")