from django.contrib import messages
from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse, HttpResponseRedirect


class Home(View):

    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        login = request.POST['login']
        password = request.POST['password']
        obj_pess_log = PessoaLogin.objects.filter(login=login, senha=password)
        if not obj_pess_log:
            messages.error(request, 'Usuário não cadastrado!')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('index')


class Index(View):

    def get(self, request):
        return render(request, 'index.html')


class Registro(View):

    def get(self, request):
        return render(request, 'registration/registro.html')


