from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import basic_information
from .calc import add
from . import gpt
from django.core import mail

class IndexView(generic.TemplateView):
    
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            email = self.request.user.email
            context = super().get_context_data(**kwargs)
            context['a'] = basic_information.objects.filter(user = email)
            return render(self.request, self.template_name, context)
        else:
            a = reverse('test:login')
            return redirect(a)  
            
        
class IndexCustomView(generic.TemplateView):
    
    template_name = 'index_custom.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            email = self.request.user.email
            context = super().get_context_data(**kwargs)
            context['a'] = basic_information.objects.filter(user = email)
            return render(self.request, self.template_name, context)
        else:
            a = reverse('test:login')
            return redirect(a)
        
    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name')
        gender = self.request.POST.get('gender')
        juusyo = self.request.POST.get('juusyo')
        moyori = self.request.POST.get('moyori')
        gakureki = self.request.POST.get('gakureki')
        sikaku1 = self.request.POST.get('sikaku1')
        sikaku2 = self.request.POST.get('sikaku2')
        sikaku3 = self.request.POST.get('sikaku3')
        like = self.request.POST.get('like')
        year1 = self.request.POST.get('year1')
        month1 = self.request.POST.get('month1')
        input1 = self.request.POST.get('input1')
        year2 = self.request.POST.get('year2')
        month2 = self.request.POST.get('month2')
        input2 = self.request.POST.get('input2')
        year3 = self.request.POST.get('year3')
        month3 = self.request.POST.get('month3')
        input3 = self.request.POST.get('input3')
        year4 = self.request.POST.get('year4')
        month4 = self.request.POST.get('month4')
        input4 = self.request.POST.get('input4')
        year5 = self.request.POST.get('year5')
        month5 = self.request.POST.get('month5')
        input5 = self.request.POST.get('input5')
        year6 = self.request.POST.get('year6')
        month6 = self.request.POST.get('month6')
        input6 = self.request.POST.get('input6')
        year7 =self.request.POST.get('year7')
        month7 = self.request.POST.get('month7')
        input7 = self.request.POST.get('input7')
        year8 = self.request.POST.get('year8')
        month8 = self.request.POST.get('month8')
        input8 = self.request.POST.get('input8')
        year9 = self.request.POST.get('year9')
        month9 = self.request.POST.get('month9')
        input9 = self.request.POST.get('input9')
        input10 = self.request.POST.get('input10')

        if input1 == None:
            input1 = ''
        if input2 == None:
            input2 = ''
        if input3 == None:
            input3 = ''
        if input4 == None:
            input4 = ''
        if input5 == None:
            input5 = ''
        if input6 == None:
            input6 = ''
        if input7 == None:
            input7 = ''
        if input8 == None:
            input8 = ''
        if input9 == None:
            input9 = ''
        if input10 == None:
            input10 = ''
        a = self.request.user
        user = a.email
        basic_information.objects.custom_any(user, name, gender, juusyo, moyori, gakureki, sikaku1, sikaku2, sikaku3, like, year1, month1,  input1, year2, month2,  input2, year3, month3,  input3, year4, month4,  input4, year5, month5,  input5, year6, month6,  input6, year7, month7,  input7, year8, month8,  input8, year9, month9,  input9, input10)
        redirect_url = reverse('profileapp:index')
        return redirect(redirect_url)

class WarekiViews(generic.TemplateView):
    template_name = 'index_wareki.html'

    def post(self, request, *args, **kwargs):
        year = int(self.request.POST.get('year'))
        month= int(self.request.POST.get('month'))
        year1 = int(year)
        if month in [1, 2, 3]:
            year -= 1
        syo_1 = str(year + 7) + '年' + ' '+ '4月'
        syo_2 = str(year + 13) + '年' + ' '+  '3月'
        tyu_1 = str(year + 13) + '年' + ' '+  '4月'
        tyu_2 = str(year + 16) + '年' + ' '+  '3月'
        kou_1 = str(year + 16) + '年' + ' '+  '4月'
        kou_2 = str(year + 19) + '年' + ' '+  '3月'
        dai_1 = str(year + 19) + '年' + ' '+  '4月'
        dai_2 = str(year + 23) + '年' + ' '+  '3月'
        sen_1 = str(year + 19) + '年' + ' '+  '4月'
        sen_2 = str(year + 21) + '年' + ' '+  '3月'
        year1 = str(year1) + '年'
        month = str(month) + '月'
        
        context = {
            'year':year1,
            'month':month,
            'syo_1':syo_1,
            'syo_2':syo_2,
            'tyu_1':tyu_1,
            'tyu_2':tyu_2,
            'kou_1':kou_1,
            'kou_2':kou_2,
            'dai_1':dai_1,
            'dai_2':dai_2,
            'sen_1':sen_1,
            'sen_2':sen_2,
            }
        return render(self.request, self.template_name, context)

class GptViews(generic.TemplateView):
    template_name = 'index_gpt.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['question'] = self.question
            context['answer'] = self.answer
            return context
        except:
            render(self.request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        self.question = self.request.POST.get('situmon')
        self.answer = gpt.call_gpt(self.request.POST.get('situmon'))
        context = self.get_context_data()
        return render(self.request, self.template_name, context)
    
class ContactViews(generic.TemplateView):
    template_name = 'index_email.html'

    def post(self, request, *args, **kwargs):
        subject = str(self.request.POST.get('subject'))
        body = str(self.request.POST.get('message'))
        to_email = str(self.request.POST.get('email'))
        email_message = mail.EmailMessage(subject=subject, body=body, bcc=['ykh2335035@stu.o-hara.ac.jp', to_email])
        email_message.send()
        context = {'any':'正常に送信されました！'}
        return render(self.request, self.template_name, context)