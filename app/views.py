from django.shortcuts import render

# Create your views here.

def form(request):
    return render(request,'form.html')

def table(request):
    return render(request,'table.html')

def table1(request):
    return render(request,'table1.html')


