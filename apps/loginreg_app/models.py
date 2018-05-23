from django.db import models
from datetime import datetime
import bcrypt
datetime.now()

class UserManager(models.Manager):
    def validateRegistration(self, postData):
        now = datetime.now()
        response = {
            'status' : False,
            'errors' : [],
        }
        if len(postData['name']) <3:
            response['errors'].append("Name too short, must be at least 3 characters")
        if len(postData['username']) <3:
            response['errors'].append("Username too short, must be at least 3 characters")
        if len(postData['password']) <8:
            response['errors'].append("Password must be at least 8 characters")
        if postData['password'] != postData['confirmpw']:
            response['errors'].append("Password and Confirm must match!")
        else:
            date_from = datetime.strptime(postData['datehired'], '%Y-%m-%d')
            if now < date_from:
                response['errors'].append('Please correct hire date!')
            if not date_from:
                reponse['errors'].append('Please input your hired date!') 
        if len(response['errors']) == 0:
            response['status'] = True
            response['user_id'] = User.objects.create(
                name=postData['name'],
                username=postData['username'],
                password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            ).id
        
        print(response)
        return response

    def validateLogin(self, postData):
        response = {
            'status' : False,
            'errors' : [],
        }
        existing_users = User.objects.filter(username=postData['username'])
        if len(existing_users) == 0:
            response['errors'].append("Sorry, try a different user name!")
        else: 
            if bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
                response['status'] = True
                response['user_id'] = existing_users[0].id

            else:
                response['errors'].append('invalid username/password combo!')
        return response

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.name, self.username, self.password)
