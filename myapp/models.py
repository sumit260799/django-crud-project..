from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    date = models.DateField()
    
    def __str__(self):
        return "%s %s %s" %(self.name, self.age, self.date)