# -*- coding: utf8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from mainapp.forms import SignUpForm, SignInForm


def view_index(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'public_html/index_loggedin.html', context)
    else:
        return render(request, 'public_html/index.html', context)


def view_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def view_sign_up(request):
    context = {}

    if request.method == 'POST':
        form = request.POST
        user = User.objects.create_user(form['username'], form['usermail'], form['userpass'])
        user.save()
        return render(request, 'public_html/sign_up_complete.html', context)
    else:
        form = SignUpForm()
        context['form'] = form
        return render(request, 'public_html/sign_up_form.html', context)


def view_sign_in(request):
    context = {}

    if request.method == 'POST':
        form = request.POST
        user = authenticate(username=form['username'], password=form['userpass'])
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'public_html/index_loggedin.html', context)
        else:
            context['form'] = SignInForm()
            context['message'] = 'Неверно введены имя пользователя и/или пароль'
            return render(request, 'public_html/sign_in_form.html', context)
    else:
        context['form'] = SignInForm()
        return render(request, 'public_html/sign_in_form.html', context)


def view_write_msg(request):
    context = {}

    if request.method == 'POST':
        pass
    else:
        pass
