from django.db import models
from django import forms
from .models import *
from college_owners.models import colleges
from super_admin.models import *
from django.core.validators import FileExtensionValidator

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))

class SignInForm(forms.Form):
    firstname = forms.RegexField(regex=r'^[a-zA-Z]+$', max_length=100, error_messages={'invalid': ("This value contain alphabets only.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'First Name'}))
    lastname = forms.RegexField(regex=r'^[a-zA-Z]+$', max_length=100, error_messages={'invalid': ("This value contain alphabets only.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    select_college = forms.ModelChoiceField(queryset=colleges.objects.all(), to_field_name='unique_id',
                                            empty_label="Select College",
                                            widget=forms.Select(attrs={'class': 'form-control'})
                                            )
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Confirm Password'}))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = faculty.objects.filter(email=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(("An user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        password = cleaned_data.get('password')

        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)

        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)

        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)

        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)

        password_confirm = cleaned_data.get('conpassword')

        if password and password_confirm:
            if password != password_confirm:
                msg = "The two password fields must match."
                self.add_error('conpassword', msg)
        return cleaned_data

class AddCourses(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Course Name'}))
    description = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Description', 'rows': '3'}))
    select_course_type = forms.ModelChoiceField(queryset=CourseType.objects.all(), to_field_name='unique_id',
                                            empty_label="Select Course Type",
                                            widget=forms.Select(attrs={'class': 'form-control'})
                                            )
    select_course_stream = forms.ModelChoiceField(queryset=CourseStream.objects.all(), to_field_name='unique_id',
                                            empty_label="Select Course Stream",
                                            widget=forms.Select(attrs={'class': 'form-control'})
                                            )
    duration_choices = [
        ('1', '1 Year'),
        ('2', '2 Year'),
        ('3', '3 Year'),
        ('4', '4 Year'),
        ('5', '5 Year'),
        ('6', '6 Year'),
        ('7', '7 Year'),
        ('8', '8 Year'),
    ]
    duration = forms.CharField(max_length=10, widget=forms.Select(choices=duration_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Course Duration' }))
