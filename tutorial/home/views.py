from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.forms import HomeForm

# Create your views here.
class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()

        context = {
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        context = {
        'form':form,
        'text':text
        }       
        return render(request, self.template_name, context)