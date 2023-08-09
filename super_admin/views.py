from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from college_owners.models import colleges, collegeOwner
from principal.models import principal
from office_administrator.models import faculty
from teacher.models import teacher

# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if superAdmin.objects.filter(email=data_record['email']) and superAdmin.objects.filter(
                    password=data_record['password']):
                user_details = superAdmin.objects.get(email=data_record['email'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['firstname'] = user_details.firstname
                    request.session['lastname'] = user_details.lastname
                    request.session['user_id'] = user_details.unique_id
                    request.session['usertype'] = 'Admin'
                    return redirect('/admin2020/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/admin2020/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/admin2020/login')
    context = {'form': form}
    return render(request, 'super_admin/login.html', context)

def signin(request):
    form = SignInForm()
    super_admin = superAdmin.objects.all()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            super_admin = superAdmin(
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email'],
            phone=data_record['phone'],
            address=data_record['address'],
            password=data_record['password'],
            status='active',
            )
            super_admin.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/admin2020/login')
    context = {'superAdmin':super_admin, 'form': form}
    return render(request, 'super_admin/signin.html', context)

def dashboard(request):
    return render(request, 'super_admin/dashboard.html')

def list_all_college_owners(request):
    college_owner_ = collegeOwner.objects.all()
    context = {'college_owner': college_owner_}
    return render(request, 'super_admin/list_college_owner.html', context)

def approve_college_owners(request,owner_id):
    collegeOwner.objects.filter(unique_id=owner_id).update(status='active')
    messages.success(request, 'Owner approved!')
    return redirect('/admin2020/list-all-college-owners')

def list_all_colleges(request):
    colleges_ = colleges.objects.all()
    context = {'colleges': colleges_}
    return render(request, 'super_admin/list_college.html', context)

def view_colleges_by_owner(request, owner_id):
    colleges_ = colleges.objects.all().filter(owner=collegeOwner.objects.get(unique_id=owner_id))
    context = {'colleges': colleges_}
    return render(request, 'super_admin/list_college.html', context)

def approve_colleges(request,college_id):
    colleges.objects.filter(unique_id=college_id).update(status='active')
    messages.success(request, 'College approved!')
    return redirect('/admin2020/list-all-colleges')

def settings_state(request):
    state_ = State.objects.all()
    form = AddStateForm()
    if request.method == 'POST':
        form = AddStateForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            state = State(
                name=data_record['state_name'],
                code=data_record['state_code'],
            )
            state.save()
            messages.success(request, 'State added successfully!')
            return redirect('/admin2020/settings/state')
    context = {'state': state_, 'form': form}
    return render(request, 'super_admin/settings_state.html', context)

def settings_city(request):
    city_ = City.objects.all()
    state_ = State.objects.all()
    form = AddCityForm()
    if request.method == 'POST':
        form = AddCityForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            city = City(
                name=data_record['city_name'],
                state=data_record['city_state'],
            )
            city.save()
            messages.success(request, 'City added successfully!')
            return redirect('/admin2020/settings/city')
    context = {'city': city_, 'state': state_, 'form': form}
    return render(request, 'super_admin/settings_city.html', context)

def settings_course_type(request):
    course_type_ = CourseType.objects.all()
    form = CourseTypeForm()
    if request.method == 'POST':
        form = CourseTypeForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            course_type = CourseType(
                name=data_record['name'],
                description=data_record['description'],
            )
            course_type.save()
            messages.success(request, 'Course type added successfully!')
            return redirect('/admin2020/settings/course-type')
    context = {'course_type': course_type_, 'form': form}
    return render(request, 'super_admin/settings_course_types.html', context)

def settings_course_stream(request):
    course_stream_ = CourseStream.objects.all()
    form = CourseStreamForm()
    if request.method == 'POST':
        form = CourseStreamForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            course_stream = CourseStream(
                name=data_record['name'],
                description=data_record['description'],
            )
            course_stream.save()
            messages.success(request, 'Course type added successfully!')
            return redirect('/admin2020/settings/course-stream')
    context = {'course_stream': course_stream_, 'form': form}
    return render(request, 'super_admin/settings_course_stream.html', context)

def settings_state_delete(request,id):
    State.objects.filter(unique_id=id).delete()
    messages.success(request, 'State deleted!')
    return redirect('/admin2020/settings/state')

def settings_city_delete(request, id):
    City.objects.filter(unique_id=id).delete()
    messages.success(request, 'City deleted!')
    return redirect('/admin2020/settings/city')

def settings_course_type_delete(request,id):
    CourseType.objects.filter(unique_id=id).delete()
    messages.success(request, 'Course stream deleted!')
    return redirect('/admin2020/settings/course-type')

def settings_course_stream_delete(request,id):
    CourseStream.objects.filter(unique_id=id).delete()
    messages.success(request, 'Course stream deleted!')
    return redirect('/admin2020/settings/course-stream')

def add_course_type(request):
    return render(request, 'super_admin/dashboard.html')

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    return redirect('/admin2020/login')


