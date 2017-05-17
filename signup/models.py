import os

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Django provides a table called user that stores basic user information like username, password and email id.
class Pcuser(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'), ('Restricted', 'Prefer not to say'))
    #username
    user = models.OneToOneField(User)
    #location
    location = models.TextField(max_length=300)
    #phone number
    phone_regex = RegexValidator(r'\+\d{8,15}$', message = "Phone number must have correct format. +999999 and up to 15 digits allowed")
    phone = models.CharField(validators=[phone_regex],blank=False, max_length=15 )
    #gender
    gender = models.CharField(max_length=10,choices = gender_choices, default='0')
    #for reset_password
    reset_pass = models.CharField(default="",max_length=320)
     
    #verification status
    #1 - unverified
    #any other number = verification code
    verified = models.CharField(max_length=100)
     
    def __unicode__(self):
        return self.user.username
        
    class Meta:
    	verbose_name = 'Pcuser'
    	verbose_name_plural = 'Pcusers'


