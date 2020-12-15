from django.shortcuts import render
from datetime import datetime

from django.views.generic import TemplateView
from main.forms import HomeForm
from .forms import InputForm 
from .forms import CustomerForm
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


class HomeView(TemplateView):
    template_name = 'main/about.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
            form = HomeForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['post']

            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)

def home_view(request): 
    context ={} 
    context['form']= InputForm() 
    return render(request, "home.html", context) 

def index(request):

	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, '', context)