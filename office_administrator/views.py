from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from college_owners.models import *
from super_admin.models import *

# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if faculty.objects.filter(email=data_record['email']) and faculty.objects.filter(
                    password=data_record['password']):
                user_details = faculty.objects.get(email=data_record['email'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['firstname'] = user_details.firstname
                    request.session['lastname'] = user_details.lastname
                    request.session['user_id'] = user_details.unique_id
                    request.session['college_id'] = user_details.college_id
                    request.session['usertype'] = 'principal'
                    return redirect('/office-administrator/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/office-administrator/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/office-administrator/login')
    context = {'form': form}
    return render(request, 'office_administrator/login.html', context)

def signin(request):
    form = SignInForm()
    faculty_ = faculty.objects.all()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            faculty_ = faculty(
            college=data_record['select_college'],
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email'],
            phone=data_record['phone'],
            address=data_record['address'],
            password=data_record['password'],
            status='pending',
            )
            faculty_.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/office-administrator/login')
    context = {'faculty':faculty_, 'form': form}
    return render(request, 'office_administrator/signin.html', context)

def dashboard(request):
    return render(request, 'office_administrator/dashboard.html')

def add_courses(request):
    form = AddCourses()
    if request.method == 'POST':
        form = AddCourses(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            courses_ = courses(
                college_id=request.session['college_id'],
                name=data_record['name'],
                course_type=data_record['select_course_type'],
                course_stream=data_record['select_course_stream'],
                description=data_record['description'],
                duration=data_record['duration'],
            )
            courses_.save()
            messages.success(request, 'Courses added successfully!')
            return redirect('/office-administrator/list-courses')
    context = {'form': form}
    return render(request, 'office_administrator/add_courses.html', context)

def list_courses(request):
    courses_ = courses.objects.all().filter(college=colleges.objects.get(unique_id=request.session['college_id']))
    context = {'courses': courses_}
    return render(request, 'office_administrator/list_courses.html', context)

def delete_courses(request, id):
    courses.objects.filter(unique_id=id).delete()
    messages.error(request, 'Courses deleted!')
    return redirect('/office-administrator/list-courses')

def add_admission(request, id):
    courses_ = courses.objects.all().filter(college=colleges.objects.get(unique_id=request.session['college_id']),unique_id=id)
    context = {'courses': courses_}
    return render(request, 'office_administrator/add_admission.html', context)

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    return redirect('/office-administrator/login')

