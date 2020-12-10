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

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

