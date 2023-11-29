from typing import Any
from django import http
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('test:password_reset_done')
    email_template_name = 'password_reset_email.html'

    def form_valid(self, form: Any):
        email = str(self.request.POST.get('email'))
        emial_hikaku = str(User.objects.filter(email=email))
        if not emial_hikaku == '<QuerySet []>':
            return super().form_valid(form)
        else:
            context = {'error':'このメールアドレスは登録されていません'}
            return render(self.request, self.template_name, context)

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name= 'password_reset_form.html'
    success_url = reverse_lazy('test:password_reset_complete')

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

class MyLoginView(generic.TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        email_ = self.request.POST.get('email')
        year = self.request.POST.get('year')
        month = self.request.POST.get('month')
        date = self.request.POST.get('date')
        password = self.request.POST.get('password')
        birthday_ = str(year) + '-' + str(month) + '-' + str(date)
        birthday = User.objects.filter(email=email_)
        count = 0
        for a in birthday:
            if str(a.birthday) == str(birthday_):
                count = 1
        if count == 1:
            user = authenticate(request, email=email_, password=password)
            if user is not None:
                login(request, user)
                a = reverse('profileapp:index')
                return redirect(a)
            else:
                a = reverse('test:login_cancel')
                return redirect(a)
        else:
            a = reverse('test:login_cancel')
            return redirect(a)
        
class Login_cancelView(generic.TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        email_ = self.request.POST.get('email')
        year = self.request.POST.get('year')
        month = self.request.POST.get('month')
        date = self.request.POST.get('date')
        password = self.request.POST.get('password')
        birthday_ = str(year) + '-' + str(month) + '-' + str(date)
        birthday = User.objects.filter(email=email_)
        count = 0
        for a in birthday:
            if str(a.birthday) == birthday_:
                count = 1
        if count == 1:
            user = authenticate(request, email=email_, password=password)
            if user is not None:
                login(request, user)
                a = reverse('profileapp:index')
                return redirect(a)
            else:
                a = reverse('test:login_cancel')
                return redirect(a)
        else:
            a = reverse('test:login_cancel')
            return redirect(a)
        
class MylogoutView(generic.TemplateView):
    template_name = 'logout.html'
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return render(request, self.template_name)

class RegisterView(generic.TemplateView):
    template_name = 'register.html'
    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        email = self.request.POST.get('email')
        email_hikaku = str(User.objects.filter(email=email))
        gender = self.request.POST.get('gender')
        year = self.request.POST.get('year')
        month = self.request.POST.get('month')
        date = self.request.POST.get('date')
        password1 = self.request.POST.get('password1')
        password2 = self.request.POST.get('password2')
        if email_hikaku == '':
            if password1 == password2:
                alphabet = 0
                number = 0
                error = 0
                password_list = list(password1)
                for i in password_list:
                    if alphabet == 1 and number == 1:
                        break
                    elif i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                        alphabet = 1
                    elif i in ['1','2','3','4','5','6','7','8','9','0']:
                        number = 1
                    else:
                        error = 1
                if len(password_list) >= 8:
                    if alphabet == 1:
                        if number == 1:
                            if not error == 1:
                                birthday = str(year) + '-' + str(month) + '-' + str(date)
                                User.objects.create_user(username=username, email=email, gender=gender, birthday=birthday, password=password1)
                                a = reverse('test:login')
                                return redirect(a)
                            else:
                                context = "アルファベット、数字以外の文字を使用しないでください。"
                                redirect_url = reverse('test:register_cancel') + f'?context={context}'
                                return HttpResponseRedirect(redirect_url)
                        else:
                            context = "数字を最低1文字以上使用してください。"
                            redirect_url = reverse('test:register_cancel') + f'?context={context}'
                            return HttpResponseRedirect(redirect_url)
                    else:
                        context = "アルファベットを最低1文字以上使用してください。"
                        redirect_url = reverse('test:register_cancel') + f'?context={context}'
                        return HttpResponseRedirect(redirect_url)                
                else:
                    context = "アルファベット、数字の2種類を使った最低8文字以上にしてください。"
                    redirect_url = reverse('test:register_cancel') + f'?context={context}'
                    return HttpResponseRedirect(redirect_url)
            else:
                context = "パスワードが一致しませんでした"
                redirect_url = reverse('test:register_cancel') + f'?context={context}'
                return HttpResponseRedirect(redirect_url)
        else:
            context = "そのメールアドレスは既に登録済みです"
            redirect_url = reverse('test:register_cancel') + f'?context={context}'
            return HttpResponseRedirect(redirect_url)
            

class Register_cancelView(generic.TemplateView):
    template_name = 'register_cancel.html'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = request.GET.get('context')
        return render(request, self.template_name, {'context':context})
    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        email = self.request.POST.get('email')
        email_hikaku = str(User.objects.filter(email=email))
        gender = self.request.POST.get('gender')
        year = self.request.POST.get('year')
        month = self.request.POST.get('month')
        date = self.request.POST.get('date')
        password1 = self.request.POST.get('password1')
        password2 = self.request.POST.get('password2')
        if email_hikaku == '':
            if password1 == password2:
                alphabet = 0
                number = 0
                error = 0
                password_list = list(password1)
                for i in password_list:
                    if alphabet == 1 and number == 1:
                        break
                    elif i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                        alphabet = 1
                    elif i in ['1','2','3','4','5','6','7','8','9','0']:
                        number = 1
                    else:
                        error = 1
                if len(password_list) >= 8:
                    if alphabet == 1:
                        if number == 1:
                            if not error == 1:
                                birthday = str(year) + '-' + str(month) + '-' + str(date)
                                User.objects.create_user(username=username, email=email, gender=gender, birthday=birthday, password=password1)
                                a = reverse('test:login')
                                return redirect(a)
                            else:
                                context = "アルファベット、数字以外の文字を使用しないでください。"
                                redirect_url = reverse('test:register_cancel') + f'?context={context}'
                                return HttpResponseRedirect(redirect_url)
                        else:
                            context = "数字を最低1文字以上使用してください。"
                            redirect_url = reverse('test:register_cancel') + f'?context={context}'
                            return HttpResponseRedirect(redirect_url)
                    else:
                        context = "アルファベットを最低1文字以上使用してください。"
                        redirect_url = reverse('test:register_cancel') + f'?context={context}'
                        return HttpResponseRedirect(redirect_url)                
                else:
                    context = "アルファベット、数字の2種類を使った最低8文字以上にしてください。"
                    redirect_url = reverse('test:register_cancel') + f'?context={context}'
                    return HttpResponseRedirect(redirect_url)
            else:
                context = "パスワードが一致しませんでした"
                redirect_url = reverse('test:register_cancel') + f'?context={context}'
                return HttpResponseRedirect(redirect_url)
        else:
            context = "そのメールアドレスは既に登録済みです"
            redirect_url = reverse('test:register_cancel') + f'?context={context}'
            return HttpResponseRedirect(redirect_url)
