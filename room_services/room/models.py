# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    mobile= models.CharField(max_length=20,null=True)
    image= models.FileField(null=True)
    gender= models.CharField(max_length=20,null=True)
    dob= models.CharField(max_length=20,null=True)
    def str(self):
        return self.user.username

class Room(models.Model):
    room_no = models.CharField(max_length=20,null=True,unique=True)
    image = models.FileField(null=True)
    type = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=20,null=True)

class Booking(models.Model):
    room_no = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    dob = models.CharField(max_length=30,null=True)
    gender = models.CharField(max_length=30,null=True)
    contact1 = models.CharField(max_length=30,null=True)
    contact2 = models.CharField(max_length=30,null=True)
    booking_date = models.CharField(max_length=30,null=True)
    total_days = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30,null=True)

class Feedback(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=40,null=True)
    contact = models.CharField(max_length=20,null=True)
    comment = models.CharField(max_length=40,null=True)