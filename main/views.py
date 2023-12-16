from django.shortcuts import render

# Create your views here.

def showdasboard(request):
    return render(request,'main/dashboard.html')

def showabout(request):
    return render(request, 'main/about_us.html')
    

def showproject(request):
    return render(request, 'main/projects.html')
    
def showevents(request):
    return render(request, 'main/events.html')
    

    
def showcontact(request):
    return render(request, 'main/contact_us.html')
    

def showteam(request):
    return render(request, 'main/ourteam.html')
    
def showfaq(request):
    return render(request,'main/faq.html')