from django.shortcuts import render

# Create your views here.

def showdasboard(request):
    context = {
        "activedash":True
    }
    return render(request,'main/dashboard.html',context)

def showabout(request):
    context = {
        "activeabout":True
    }
    return render(request, 'main/about_us.html',context)
    

def showproject(request):
    context = {
        "activeproject":True
    }
    return render(request, 'main/projects.html',context)
    
    
def showevents(request):
    context = {
        "activeevent":True
    }
    return render(request, 'main/events.html',context)
    

    
def showcontact(request):
    context = {
        "activecontact":True
    }
    return render(request, 'main/contact_us.html',context)
    

def showteam(request):
    context = {
        "activeteam":True
    }
    return render(request, 'main/ourteam.html',context)
    
def showfaq(request):
    context = {
        "activeexplore":True
    }
    return render(request, 'main/faq.html', context)
    
def show404(request, exception):
    return render (request,'main/404.html',status=404)