from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

from django.http import HttpResponseRedirect
from .forms import ProductForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Yout acccount has been created? Now you able to login {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,

    }

    return render(request, 'user/profile.html', context)




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

    return render(request, 'profile.html', {'form': form})

def index(request):
    questions=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        questions = Queries.objects.filter(query__icontains=search)

        name = request.GET.get('name')
        query = Queries.object.create(query=search, user_id=name)
        query.save()

    return render(request, 'templates/profile.html',{
        'questions': questions,
    })

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context ={
        'form': form
    }
    return render (request, "user/product_create.html", context)