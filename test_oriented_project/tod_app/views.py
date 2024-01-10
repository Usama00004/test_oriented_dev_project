from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import MyModelForm

def author_form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyModelForm()

    return render(request, 'author.html', {'form': form})



def home(request):
    return render(request, 'home.html')
