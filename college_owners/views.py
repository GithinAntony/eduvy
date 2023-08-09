from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
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
            if collegeOwner.objects.filter(email=data_record['email']) and collegeOwner.objects.filter(
                    password=data_record['password']):
                user_details = collegeOwner.objects.get(email=data_record['email'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['firstname'] = user_details.firstname
                    request.session['lastname'] = user_details.lastname
                    request.session['user_id'] = user_details.unique_id
                    request.session['usertype'] = 'owner'
                    return redirect('/college-owners/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/college-owners/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/college-owners/login')
    context = {'form': form}
    return render(request, 'college_owners/login.html', context)

def signin(request):
    form = SignInForm()
    college_owner = collegeOwner.objects.all()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            college_owner = collegeOwner(
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email'],
            phone=data_record['phone'],
            address=data_record['address'],
            password=data_record['password'],
            status='pending',
            )
            college_owner.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/college-owners/login')
    context = {'collegeOwner':college_owner, 'form': form}
    return render(request, 'college_owners/signin.html', context)

def edit_profile(request):
    form = EditProfile()
    userdata = collegeOwner.objects.get(unique_id=request.session['user_id'])
    form = EditProfile(initial={'firstname': userdata.firstname,'lastname': userdata.firstname, 'phone':userdata.phone, 'email': userdata.email, 'address': userdata.address})
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, user_id=request.session['user_id'])
        if form.is_valid():
            uploaded_file = request.FILES['profile_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            data_record = form.cleaned_data
            flag = 0
            mess = ''
            if flag == 0:
                record = collegeOwner.objects.get(unique_id=request.session['user_id'])
                record.firstname = data_record['firstname']
                record.lastname = data_record['lastname']
                record.phone = data_record['phone']
                record.email = data_record['email']
                record.address = data_record['address']
                record.photo = fs.url(file_name)
                record.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('/college-owners/edit-profile')
            else:
                messages.success(request, mess)
    context = {'form': form}
    return render(request, 'college_owners/edit-profile.html', context)

def dashboard(request):
    return render(request, 'college_owners/dashboard.html')

def list_college(request):
    colleges_ = colleges.objects.all().filter(owner=collegeOwner.objects.get(unique_id=request.session['user_id']))
    context = {'colleges': colleges_}
    return render(request, 'college_owners/list_college.html', context)

def add_college(request):
    form = AddCollegeForm()
    colleges_ = colleges.objects.all()
    if request.method == 'POST':
        form = AddCollegeForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            colleges_ = colleges(
                owner_id=request.session['user_id'],
                name=data_record['name'],
                phone=data_record['phone'],
                website=data_record['website'],
                email=data_record['email'],
                address=data_record['address'],
                city=data_record['select_city'],
                state=data_record['select_state'],
                course_type=data_record['select_course_type'],
                status='pending',
            )
            colleges_.save()
            messages.success(request, 'College added successfully!')
            return redirect('/college-owners/list-college')
    context = {'colleges': colleges_, 'form': form}
    return render(request, 'college_owners/add_college.html', context)

def user_hierarchy(request, college_id):
    principal_ = principal.objects.all().filter(college_id=college_id)
    faculty_ = faculty.objects.all().filter(college_id=college_id)
    teacher_ = teacher.objects.all().filter(college_id=college_id)
    context = { 'college_id':college_id, 'principal': principal_, 'faculty': faculty_, 'teacher': teacher_ }
    return render(request, 'college_owners/user_hierarchy.html', context)

def principal_approve(request, college_id, user_id):
    principal.objects.filter(unique_id=user_id).update(status='active')
    messages.success(request, 'Principal approved!')
    return redirect('/college-owners/user-hierarchy/'+str(college_id))

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    return redirect('/college-owners/login')

