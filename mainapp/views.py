# -*- coding: utf8 -*-
from smtplib import SMTPException

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from mainapp.forms import SignUpForm, SignInForm, WriteMsgForm
from mainapp.models import MsgModel


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
        # msg = MsgModel()
        # msg.user = request.user
        # msg.msg_text = request.POST.get('msg_text')
        msg = MsgModel(user=request.user, msg_text=request.POST.get('msg_text'))
        msg.clean_fields()
        msg.save()
        try:
            send_mail(
                subject='Тестовое письмо из Django',
                message=msg.msg_text,
                from_email=None,
                recipient_list=['nikluxomaklay@gmail.com'],
                fail_silently=False,
            )
            msg.is_sent = True
            msg.save()
        except SMTPException, e:
            pass

        return render(request, 'public_html/msg_sent.html')
    else:
        context['form'] = WriteMsgForm()
        return render(request, 'public_html/write_msg_form.html', context)
