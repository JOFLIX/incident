from django.db import models
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class TicketSubType(models.Model):
    nametype=models.CharField(max_length=15)


    def __str__(self):

        return self.nametype


class TicketType(models.Model):
    Critical = 1
    High = 2
    Normal = 3
    Low = 4
    Very_Low=5


    PRIORITY_CHOICES=(
        (Critical,'1. Critical'),
        (High,'2. High'),
        (Normal,'3. Normal'),
        (Low,'4. Low'),
        (Very_Low,'5. Very Low'),
    )

    name=models.CharField(max_length=15)
    namesubtype=models.ManyToManyField(TicketSubType)
    priority=models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3,
        blank=3,
        
    )

    def __str__(self):
        return self.name

class Department(models.Model):

    department_name=models.CharField(max_length=30)
    department_description=models.TextField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.department_name} Department'
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='naomi.jpg',upload_to='profile_pics')
    phone_number = PhoneNumberField(blank=True,null=True)
    department=models.ForeignKey(Department,on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'










