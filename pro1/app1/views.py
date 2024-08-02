from django.shortcuts import render,redirect
from .forms import ClientForm
from .models import Client

# Create your views here.
def cview(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/client.html",{"form":form})

def sview(request):
    obj = Client.objects.all()
    return render(request,"app1/show.html",{"obj":obj})

def uview(request,pk):
    obj = Client.objects.get(id=pk)
    form = ClientForm(instance=obj)
    if request.method == "POST":
        form = ClientForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/client.html",{"form":form})

def dview(request,k):
    obj = Client.objects.get(id=k)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})

def hview(request):
    return render(request,"app1/home.html",{})