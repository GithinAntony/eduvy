from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if teacher.objects.filter(email=data_record['email']) and teacher.objects.filter(
                    password=data_record['password']):
                user_details = teacher.objects.get(email=data_record['email'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['firstname'] = user_details.firstname
                    request.session['lastname'] = user_details.lastname
                    request.session['user_id'] = user_details.unique_id
                    request.session['college_id'] = user_details.college_id
                    request.session['usertype'] = 'principal'
                    return redirect('/teacher/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/teacher/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/teacher/login')
    context = {'form': form}
    return render(request, 'teacher/login.html', context)

def signin(request):
    form = SignInForm()
    teacher_ = teacher.objects.all()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            teacher_ = teacher(
            college=data_record['select_college'],
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email'],
            phone=data_record['phone'],
            address=data_record['address'],
            password=data_record['password'],
            status='pending',
            )
            teacher_.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/teacher/login')
    context = {'teacher':teacher_, 'form': form}
    return render(request, 'teacher/signin.html', context)

def dashboard(request):
    return render(request, 'teacher/dashboard.html')

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    return redirect('/teacher/login')

