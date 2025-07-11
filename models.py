from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    age= models.IntegerField() 
    section = models.CharField(max_length=1)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, default='0000000000')

    def __str__(self):
        return self.name
