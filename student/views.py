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
            if students.objects.filter(email=data_record['email']) and students.objects.filter(
                    password=data_record['password']):
                user_details = students.objects.get(email=data_record['email'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['firstname'] = user_details.firstname
                    request.session['lastname'] = user_details.lastname
                    request.session['user_id'] = user_details.unique_id
                    return redirect('/student/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/student/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/student/login')
    context = {'form': form}
    return render(request, 'student/login.html', context)

def signin(request):
    form = SignInForm()
    student_ = students.objects.all()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            student_ = students(
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email'],
            phone=data_record['phone'],
            address=data_record['address'],
            password=data_record['password'],
            status='active',
            )
            student_.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/student/login')
    context = {'principal':student_, 'form': form}
    return render(request, 'student/signin.html', context)

def dashboard(request):
    return render(request, 'student/dashboard.html')

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    return redirect('/student/login')

