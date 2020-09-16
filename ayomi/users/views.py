from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
import json


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'users/register.html', {'form': form})

    form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def change_user_info(request):
    if request.method == 'POST':
        try:
            query_dict = request.POST
            current_user = User.objects.get(pk=request.user.id)
            current_user.email = query_dict['email']
            current_user.first_name = query_dict['firstName']
            current_user.last_name = query_dict['lastName']
            current_user.save()
            response = {'succeed': True}
        except Exception as e:
            print(e)
            response = {'succeed': True}

        return HttpResponse(json.dumps(response))
    else:
        return HttpResponseForbidden()
