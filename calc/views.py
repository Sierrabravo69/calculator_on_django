from django.shortcuts import render

# Create your views here.
def cal(req):
    return render(req,'index.html')