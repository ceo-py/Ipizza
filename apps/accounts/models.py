from django.contrib.auth.models import AbstractUser
from django.db import models


# class CustomUser(AbstractUser):
#     address = models.CharField(max_length=100,
#                                verbose_name='Адрес')
#     first_name = models.CharField(max_length=20,
#                                   verbose_name='Име')
#     last_name = models.CharField(max_length=20,
#                                  verbose_name='Фамилия')
#     phone_number = models.CharField(max_length=12,
#                                     verbose_name='Телефон')
#
#     email = models.EmailField(max_length=20,
#                               verbose_name='Email адрес')
#
#     def __str__(self):
#         return self.username


# class UserRegistrationForm(CustomUser):
    # class Meta:
    #     model = CustomUser
    #     fields = ['email', 'password1', 'password2']
