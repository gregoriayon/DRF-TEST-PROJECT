from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# Generating tokens by using signals
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print("sender", sender)
    if created:
        Token.objects.create(user=instance)
        print('Token created successfully!')



class StudentsModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    roll = models.CharField(max_length=255, null=True)
    mark = models.PositiveIntegerField(blank=True)
    email = models.EmailField(max_length=255, null=True)
    details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
    


@receiver(post_save, sender=StudentsModel) 
def create_profile(sender, instance, created, **kwargs):
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    print("kwargs", kwargs)
    if created:
        print("After save!")



class EmployeeModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True)
    salary = models.FloatField(blank= True, default=0.0)
    department = models.CharField(max_length=255, null=True)


    def __str__(self):
        return f"{self.id} - {self.name}"
    

    
class PersonModel(models.Model):
    name = models.CharField(max_length=115, null=True)
    age = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.name}"
    

class PlayerModel(models.Model):
    name = models.CharField(max_length=115, null=True)
    age = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"Player: {self.id} - {self.name}"
    


# Model create for Serializer relations
class Singer(models.Model):
    name = models.CharField(max_length=115, null=True)
    gender = models.CharField(max_length=115, null=True)

    def __str__(self):
        return f"Singer: {self.id} - {self.name}"
    

class Song(models.Model):
    title = models.CharField(max_length=115, null=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, null=True, related_name='songs')
    duration = models.IntegerField()

    def __str__(self):
        return f"Song: {self.id} - {self.title}"