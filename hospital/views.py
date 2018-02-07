from django.shortcuts import render
import os

# Create your views here.
def test(request):
    if request.method == 'POST':
        img = request.FILES.get('img','')
        f = open(os.path.join('static', img.name), 'wb')
        for chunk in img.chunks(chunk_size=1024):
             f.write(chunk)
        f.close()
    return render(request, 'test.html')

def login(request):
    return render(request,'login.html')

def index(request):
    if request.method=='POST':
        title = request.POST.get('title','')
        context = request.POST.get('context','')
        subject = request.POST.get('subject', '')
        print(title,context,subject)
    return render(request, 'index.html')

def profile(request):
    return render(request, 'pages-profile.html')

def table(request):
    return render(request, 'table-basic.html')

def detail(request):
    return render(request, 'detail.html')

def news(request):
    return render(request, 'news.html')

def newsdetail(request):
    return render(request, 'news-detail.html')

def adminhandle(request):
    return render(request, 'admin-handle.html')

def adminhandled(request):
    return render(request, 'admin-handled.html')

def admindown(request):
    return render(request, 'admin-down.html')

def admindetail(request):
    return render(request, 'admin-detail.html')

def doctorhandle(request):
    return render(request, 'doctor-handle.html')

def doctorhandled(request):
    return render(request, 'doctor-handled.html')

def doctordetail(request):
    return render(request, 'doctor-detail.html')