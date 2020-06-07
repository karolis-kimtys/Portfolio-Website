from django.db import models
from django.conf import settings
# from django.contrib.auth.models import AbstractBaseUser, User

# Create your models here.

# class UserProfile(AbstractBaseUser):
#     first_name = models.CharField(max_length = 128, blank = True)
#     last_name = models.CharField(max_length = 128, blank = True)
#     email = models.EmailField(max_length = 264, unique = True)
#     username = models.CharField(max_length = 128, unique=True, primary_key=True)
#     password = models.CharField(max_length = 50)

#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.username

# class UserProfileInfo(models.Model):

#     username = models.OneToOneField(User, on_delete=models.PROTECT)

#     def __str__(self):
#         return self.user.username
