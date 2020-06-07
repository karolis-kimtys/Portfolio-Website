from django.shortcuts import render, redirect
from django.contrib import messages
from registration import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# from registration.models import UserProfile
# from registration.forms import UserForm

# @login_required
# def signout(request):
#     logout(request)
#     messages.info(request, 'You have signed out!')
#     return HttpResponseRedirect(reverse('index'))

# def signup(request):
#     registered = False
#     if request.method == "POST":
#         user_form = UserForm(data = request.POST)

#         if user_form.is_valid():
#             user = user_form.save(commit=True)
#             # user.first_name = user_form.cleaned_data.get('first_name')
#             # user.last_name = user_form.cleaned_data.get('last_name')
#             # user.email = user_form.cleaned_data.get('email')
#             # username = user_form.cleaned_data.get('username')
#             # password = user_form.cleaned_data.get('password')

#             # authenticate(username=username, password=password)

#             user.set_password(user.password)

#             user.save()
#             registered = True
#             print("New sign up")
#             messages.info(request, 'You have signed up!')
#             return redirect('index')
#         else:
#             messages.info(request, 'Something is wrong!')
#             form = UserForm()
#             print(user_form.errors)

#     else:
#         user_form = UserForm()

#     return render(request, 'signup.html',
#                                 {'user_form' : user_form,
#                                  'registered' : registered})


# def signin(request):
#     if request.method == "POST":
#         # First get the username and password supplied
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Django's built-in authentication function:
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 messages.info(request, 'You have signed in!')
#                 return HttpResponseRedirect(reverse('index'))
#                 print(username, " has signed up")
#             else:
#                 messages.info(request, 'Your account is not active!')
#                 return render(request, "signin.html")
#         else:
#             print("Username: {} and Password: {} tried to log in!".format(username, password))
#             messages.info(request, 'Your account details have not been found. Please Sign Up!')
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         return render(request, "signin.html")
