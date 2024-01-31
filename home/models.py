from django.db import models

# Create your models here.


    
class Car(models.Model):
    model = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model
    
class Person(models.Model):
    car = models.ForeignKey(Car,null=True,blank=True,on_delete=models.CASCADE,related_name='car')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name