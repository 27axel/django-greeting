from django.shortcuts import render, redirect
from .forms import NameForm
from .models import UserName


def home(request):
    latest_user = UserName.objects.last()

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            UserName.objects.create(name=name)
            return redirect('welcome')
    else:
        form = NameForm()

    return render(request, 'greeting/home.html', {
        'form': form,
        'latest_user': latest_user,
    })


def welcome(request):
    latest_user = UserName.objects.last()
    if not latest_user:
        return redirect('home')
    return render(request, 'greeting/welcome.html', {'name': latest_user.name})
