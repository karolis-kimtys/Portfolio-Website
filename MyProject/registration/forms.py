from django import forms
from django.core import validators
# from registration.models import UserProfile
# from django.contrib.auth.models import User


# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with letter 'z'.")
#
# class FormName(forms.Form):
#     # first_name = forms.CharField(validators = [check_for_z])
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#
#     verify_email = forms.EmailField(label = "Verify your email:")
#     botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']
#
#         if email != vmail:
#             raise forms.ValidationError('Emails do not match!')

# class NewUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

#Below code to be inserted to HTML for User Sign Up/In Button
        #   <li class="nav-item">
        #     <button id = "navbtn" onclick="location.href='{% url 'registration:signup' %}'" class="btn"">Sign Up</button>
        #   </li>

        #   {% if user.is_authenticated %}
        #   <li class="nav-item active ">
        #     <button id = "navbtn" onclick="location.href='{% url 'registration:signout' %}'" class="btn" type="button">Sign Out</button>
        #   </li>

        #   {% else %}
        #   <li class="nav-item active">
        #     <button id = "navbtn" onclick="location.href='{% url 'registration:signin' %}'" class="btn" type="button">Sign In</button>
        #   </li>
        #   {% endif %}

# class UserForm(forms.ModelForm):
#     # first_name = forms.CharField(max_length = 128, help_text = 'First Name')
#     # last_name = forms.CharField(max_length = 128, help_text = 'Last Name')
#     # email = forms.EmailField(max_length = 264, help_text = 'E-mail')
#     password = forms.CharField(widget = forms.PasswordInput)

#     class Meta():
#         model = UserProfile
#         fields = ('first_name', 'last_name', 'username', 'email', 'password')

