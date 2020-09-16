from django.shortcuts import render

from django.http import HttpResponseRedirect

from users.forms import ChangeUserDataForm


def home(request):
    form = ChangeUserDataForm()
    return render(request, 'website/home.html', {'form': form})
