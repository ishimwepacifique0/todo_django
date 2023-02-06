from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username and password")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'You have logged out a few momemt ago')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    number = StudentData.objects.count()
    select = StudentData.objects.all()
    print(select)
    return render(request,'dashboard.html',{"data":number,"data2":select})


@login_required(login_url='login')
def manage_student(request):
    number = StudentData.objects.count()
    select = StudentData.objects.all()
    return render(request,'manage_student.html',{"data":select,"number":number})

@login_required(login_url='login')
def create_student(request):
    dataedit = StudentData.objects.count()
    select = StudentData.objects.all()
    if request.method == 'POST':
        saveDate = StudentData()
        x = datetime.datetime.now()
        saveDate.StudentName = request.POST['studentname']
        saveDate.Option = request.POST['option']
        saveDate.Date = request.POST['date']
        saveDate.Level = request.POST['level']
        saveDate.Gender = request.POST['gender']
        saveDate.Academic_year = request.POST['academic_year']
        saveDate.Expired = x.strftime("2024-%m-%d")
        saveDate.Request = request.POST['request']
        saveDate.save()
    return render(request,'new_student.html',{"dataedit":dataedit,"data2":select})


@login_required(login_url='login')
def delete_student(request,id):
    getId = StudentData.objects.get(id=id)
    getId.delete()
    return redirect('manage_student')


@login_required(login_url='login')
def edit_student(request,id):
    dataedit = StudentData.objects.count()
    select = StudentData.objects.all()
    getId = StudentData.objects.get(id=id)
    if request.method == 'POST':
        x = datetime.datetime.now()
        getId.StudentName = request.POST['studentname']
        getId.Option = request.POST['option']
        getId.Date = request.POST['date']
        getId.Level = request.POST['level']
        getId.Gender = request.POST['gender']
        getId.Academic_year = request.POST['academic_year']
        getId.Expired = x.strftime("2024-%m-%d")
        getId.Request = request.POST['request']

        valid = getId.save()
        if valid is not None:
            return redirect('manage_student')
    return render(request,'edit_student.html',{"data":getId,"dataedit":dataedit,"data2":select})


def send_request(request):
    if request.method == 'POST':
        x = datetime.datetime.now()
        saveDate = StudentData()
        saveDate.StudentName = request.POST['studentname']
        saveDate.Option = request.POST['option']
        saveDate.Date = request.POST['date']
        saveDate.Level = request.POST['level']
        saveDate.Gender = request.POST['gender']
        saveDate.Academic_year = request.POST['academic_year']
        saveDate.Expired = x.strftime("2024-%m-%d")
        saveDate.Request  =  request.POST['request']
        submit = saveDate.save()
        if submit is True:
            messages.success(request,'Data sent to Administration wait for response')
    return render(request,'send_request.html')
