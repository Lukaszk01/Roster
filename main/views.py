from django.shortcuts import render
from datetime import datetime
# Create your views here.



def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def testView(request):
    current_user = request.user
    context = {'username': current_user.username, 'current_user': current_user}
    return render(request, 'main/test.vue', context)

def management(request):
    return render(request, 'main/management.html', {'title': 'management'})
    
def notifications(request):
    return render(request, 'main/notifications.html', {'title': 'notifications'})

