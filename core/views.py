from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

class Home(View):

    def get(self, request):
        return render(request, 'registration/login.html', context={"Nome": 'doglas'})

    def post(self, request):
        login = request.POST['login']
        password = request.POST['password']
        ObjPessLog = PessoaLogin.objects.filter(login=login, senha=password)
        if not ObjPessLog:
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('index')


class Index(View):

    def get(self, request):
        return render(request, 'index.html')


class Login(View):

    def get(self, request):
        return render(request, 'registration/login.html')


    def ramon(self, request):
        return render(request, 'static/ramonzera.jpeg')
