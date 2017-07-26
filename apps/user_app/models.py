from __future__ import unicode_literals
from django.db import models
import bcrypt, re


# Create your models here.
class UserManager(models.Manager):
    def create_user(self, data):
        errors = {}
        if not data['name'] or len(data['name']) < 3 or not data['username'] or len(data['username']) < 3:
            errors['name'] = 'Invalid Name, must be at least 3 characters'
        if self.filter(username=data['username']):
            errors['username_exist'] = 'Username exist already, pick another'
        if not data['password'] or len(data['password']) < 8:
            errors['password'] = 'Invalid password'
        if data['password'] != data['confirm_password']:
            errors['confirm_password'] = 'password doesnt match'
        if len(errors):
            return errors
        else:
            hash_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            return self.create(name=data['name'], username=data['username'], password=hash_password)

    def validate_user(self, data):
        errors = {}
        if self.filter(username=data['username']):
            user = self.get(username=data['username'])
            hash_password = bcrypt.hashpw(data['password'].encode(), user.password.encode())
            if hash_password == user.password:
                return user
            else:
                errors['password'] = 'Invalid password'
        else:
            errors['username'] = 'Invalid username'
        return errors



class User(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()
