from django.shortcuts import render, redirect
from .models import *
from college_owners.models import colleges
from office_administrator.models import faculty
from teacher.models import teacher
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
            if principal.objects.filter(email=data_record['email']) and principal.objects.filter(
                    password=data_record['password']):
                user_details = principal.objects.get(email=data_record['email'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['firstname'] = user_details.firstname
                    request.session['lastname'] = user_details.lastname
                    request.session['user_id'] = user_details.unique_id
                    request.session['college_id'] = user_details.college_id
                    request.session['usertype'] = 'principal'
                    return redirect('/principal/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/principal/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/principal/login')
    context = {'form': form}
    return render(request, 'principal/login.html', context)

def signin(request):
    form = SignInForm()
    principal_ = principal.objects.all()
    colleges_ = colleges.objects.all()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            principal_ = principal(
            college=data_record['select_college'],
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email'],
            phone=data_record['phone'],
            address=data_record['address'],
            password=data_record['password'],
            status='pending',
            )
            principal_.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/principal/login')
    context = {'principal':principal_, 'colleges':colleges_, 'form': form}
    return render(request, 'principal/signin.html', context)

def dashboard(request):
    return render(request, 'principal/dashboard.html')

def faculty_hierarchy(request):
    faculty_ = faculty.objects.all().filter(college=colleges.objects.get(unique_id=request.session['college_id']))
    teacher_ = teacher.objects.all().filter(college=colleges.objects.get(unique_id=request.session['college_id']))
    context = {'college_id': request.session['college_id'], 'faculty': faculty_, 'teacher': teacher_}
    return render(request, 'principal/user_hierarchy.html', context)

def faculty_approve(request, user_id):
    faculty.objects.filter(unique_id=user_id).update(status='active')
    messages.success(request, 'faculty approved!')
    return redirect('/principal/faculty-hierarchy')

def teacher_approve(request, user_id):
    teacher.objects.filter(unique_id=user_id).update(status='active')
    messages.success(request, 'teacher approved!')
    return redirect('/principal/faculty-hierarchy')

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    return redirect('/principal/login')

