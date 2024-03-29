from django.db import models
from datetime import date, datetime
# validation and authintication file which had made by Ali
from .ValidAuth import *

# for json problem to store Json in DB 
from django.contrib.postgres.fields import JSONField

"""
sigeUP:::

firstName_signUp
lastName_signUp
email_signUp
password_signUp
confirmPassword_signUp
_________________________
Login::::
email_login
password_login

"""
# This is the Vaildation


class UsersManager(models.Manager):
    def basic_validator(self, postData):  # for testing
        errors = {}
        # vaildation for SignUp
        # first name characters only and more at least 2 characters
        if not isItValidName(str(postData["firstName_signUp"])):
            errors["firstName_signUp"] = "Please Enter Your Real First Name"
        # last name characters only and more at least 2 characters
        if not isItValidName(str(postData["lastName_signUp"])):
            errors["lastName_signUp"] = "Please Enter Your Real Last Name"
        # is the Email in Email fromat ?
        if not isItValidEmail(str(postData["email_signUp"])):
            errors["email_signUp"] = "Please Enter Valid Email"
        # check the Email not exisit in DB
        if len(Users.objects.filter(email=str(postData["email_signUp"]).lower())) > 0:
            errors["email_signUp"] = "This Email Already Reigistered || Email already in DB"
        # password must be VERY STRONG
        # length minimum 8 characters at least one digit, lowerrcase, uppercase, and special
        if not isVeryStrongPassword(str(postData["password_signUp"])):
            errors["password_signUp"] = "Password Must be : length minimum 8 characters. at least one digit, lowerrcase, uppercase, and special"

        # check the password is same for confirmation
        if str(postData["password_signUp"]) != str(postData["confirmPassword_signUp"]):
            errors["confirmPassword_signUp"] = "Password is not same"

        return errors


class Users(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, null=True)
    password = models.TextField()
    is_admin = models.BooleanField(default=False)
    # for Vaildation part
    objects = UsersManager()

class Reports_result(models.Model): # Ali dictonaries
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # Registered user ID
    dict_report= JSONField() # JSon Vield for DataReport_API

class Messages(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # sender ID
    title = models.CharField(max_length=255) 
    message = models.TextField()
    replay = models.TextField(default="")  # FOR
    isRead=models.BooleanField(default=True) # FOR USER Auto change by view button
    
