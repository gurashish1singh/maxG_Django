from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):


    context = {
        'title' : 'Home'
    }
    template_name = 'accounts/home.html'
    return render(request,template_name,context)


def login_redirect(request):
    return redirect('/accounts/login')


def register(request):

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/accounts/')
    else:
        form = UserCreationForm()


    context = {
        'title' : 'Register Page',
        'form' : form,
    }
    template_name = 'accounts/register.html'
    return render(request,template_name,context)


