from django.shortcuts import render

# Create your views here.
def prabhas(request):
    return render(request,('prabhas.html'))
def yogi(request):
    return render(request,'yogi.html')
