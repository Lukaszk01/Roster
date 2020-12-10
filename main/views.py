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

def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {
            'form': form, 'posts': posts, 'users': users, 'friends': friends
        }
        return render(request, self.template_name, args)