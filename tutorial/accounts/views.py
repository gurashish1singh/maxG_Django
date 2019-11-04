from django.shortcuts import render

# Create your views here.
def home(request):


    context = {
        'title' : 'Home'
    }
    template_name = 'accounts/home.html'
    return render(request,template_name,context)


# def login(request):


#     context = {
#         'title' : 'Login Page'
#     }
#     template_name = 'accounts/login.html'
#     return render(request,template_name,context)


