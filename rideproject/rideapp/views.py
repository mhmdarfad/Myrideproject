from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Person


# Create your views here.
def home(request):
    obj = Place.objects.all()
    orj = Person.objects.all()
    return render(request, "index.html", {'result': obj,'results':orj})
    # return render(request, "index.html", {'results': orj})

# ,{'obj':name})

# def addition(request):
# x=int(request.GET['num1'])
#  y=int(request.GET['num2'])
#   add=x+y
#    minus = x - y
#  mult=x*y
#   div=x//y
#    return render(request,"result.html",{'addi':add,'min':minus,'multi':mult,'divi':div})


# def about(request):
#   return render(request, "about.html")


# def contact(request):
#  return HttpResponse("contact details")

# def detail(request):
#   return render(request,"detail.html")

# def thanks(request):
#   return HttpResponse("Thank you all")
