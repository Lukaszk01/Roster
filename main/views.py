from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def testView(request):
    current_user = request.user
    context = {'username': current_user.username, 'current_user': current_user}
    return render(request, 'main/test.html', context)