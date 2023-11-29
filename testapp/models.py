from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class basic_informationManager(BaseUserManager):

    def custom_any(self, user, name, gender, juusyo, moyori, gakureki, sikaku1, sikaku2, sikaku3, like, year1, month1, input1, year2, month2, input2, year3, month3, input3, year4, month4, input4, year5, month5, input5, year6, month6, input6, year7, month7, input7, year8, month8, input8, year9, month9, input9, input10):
        try:
            a = basic_information.objects.get(user = user)
            a.user = user
            a.name = name
            a.gender = gender
            a.juusyo = juusyo
            a.moyori = moyori
            a.gakureki = gakureki
            a.sikaku1 = sikaku1
            a.sikaku2 = sikaku2
            a.sikaku3 = sikaku3
            a.like = like
            a.year1 = year1
            a.month1 = month1 
            a.input1 = input1
            a.year2 = year2
            a.month2 = month2 
            a.input2 = input2
            a.year3 = year3
            a.month3 = month3 
            a.input3 = input3
            a.year4 = year4
            a.month4 = month4 
            a.input4 = input4
            a.year5 = year5
            a.month5 = month5 
            a.input5 = input5
            a.year6 = year6
            a.month6 = month6 
            a.input6 = input6
            a.year7 = year7
            a.month7 = month7 
            a.input7 = input7
            a.year8 = year8
            a.month8 = month8 
            a.input8= input8
            a.year9 = year9
            a.month9 = month9 
            a.input9 = input9
            a.input10 = input10
            a.save(using=self._db)
            return a
        except:
            custom_any = self.model(
            user = user,
            name = name,
            gender = gender,
            juusyo = juusyo,
            moyori = moyori,
            gakureki = gakureki,
            sikaku1 = sikaku1,
            sikaku2 = sikaku2,
            sikaku3 = sikaku3,
            like = like,
            year1 = year1,
            month1 = month1,
            input1 = input1,
            year2 = year2,
            month2 = month2,
            input2 = input2,
            year3 = year3,
            month3 = month3,
            input3 = input3,
            year4 = year4,
            month4 = month4,
            input4 = input4,
            year5 = year5,
            month5 = month5,
            input5 = input5,
            year6 = year6,
            month6 = month6,
            input6 = input6,
            year7 = year7,
            month7 = month7,
            input7 = input7,
            year8 = year8,
            month8 = month8,
            input8= input8,
            year9 = year9,
            month9 = month9,
            input9 = input9,
            input10 = input10
            )
            custom_any.save(using=self._db)
            return custom_any

class basic_information(models.Model):

    user = models.CharField(max_length=200)

    name = models.CharField(max_length=200, null=True)
    gender = models.TextField(max_length=10, null=True)
    juusyo = models.CharField(max_length=200, null=True)
    moyori = models.CharField(max_length=200, null=True)
    gakureki = models.CharField(max_length=200, null=True)
    sikaku1 = models.CharField(max_length=200, null=True)
    sikaku2 = models.CharField(max_length=200, null=True)
    sikaku3 = models.CharField(max_length=200, null=True)
    like = models.CharField(max_length=200, null=True)
    year1 = models.CharField(max_length=8, null=True)
    month1 = models.CharField(max_length=8, null=True)
    input1 = models.CharField(max_length=200, null=True)
    year2 = models.CharField(max_length=8, null=True)
    month2 = models.CharField(max_length=8, null=True)
    input2 = models.CharField(max_length=200, null=True)
    year3 = models.CharField(max_length=8, null=True)
    month3 = models.CharField(max_length=8, null=True)
    input3 = models.CharField(max_length=200, null=True)
    year4 = models.CharField(max_length=8, null=True)
    month4 = models.CharField(max_length=8, null=True)
    input4 = models.CharField(max_length=200, null=True)
    year5 = models.CharField(max_length=8, null=True)
    month5 = models.CharField(max_length=8, null=True)
    input5 = models.CharField(max_length=200, null=True)
    year6 = models.CharField(max_length=8, null=True)
    month6 = models.CharField(max_length=8, null=True)
    input6 = models.CharField(max_length=200, null=True)
    year7 = models.CharField(max_length=8, null=True)
    month7 = models.CharField(max_length=8, null=True)
    input7 = models.CharField(max_length=200, null=True)
    year8 = models.CharField(max_length=8, null=True)
    month8 = models.CharField(max_length=8, null=True)
    input8 = models.CharField(max_length=200, null=True)
    year9 = models.CharField(max_length=8, null=True)
    month9 = models.CharField(max_length=8, null=True)
    input9 = models.CharField(max_length=200, null=True)
    input10 = models.CharField(max_length=200, null=True)

    objects = basic_informationManager()