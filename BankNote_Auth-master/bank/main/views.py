from django.shortcuts import render
from .ml import *
# Create your views here.

def test(request):
    if request.method == "POST":
        varience = float(request.POST["varience"])
        skewness = float(request.POST["skewness"])
        curtosis = float(request.POST["curtosis"])
        entropy = float(request.POST["entropy"])
        
        if is_authentic(varience, skewness, curtosis, entropy) == 1:
            return render(request, "banknote.html", {"response":"yes its authentic"})
        else:
            return render(request, "banknote.html", {"response":"Nope its fake"})
    else:
        return render(request, "banknote.html")