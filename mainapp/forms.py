# -*- coding: utf8 -*-
from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=255)
    usermail = forms.EmailField(label='E-mail')
    userpass = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class SignInForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=255)
    userpass = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class WriteMsgForm(forms.Form):
    msg_text = forms.CharField(label='Сообщение', widget=forms.Textarea)