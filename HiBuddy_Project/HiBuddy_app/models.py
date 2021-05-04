from django.db import models
from .utils import *

# Create your models here.

# 1.================================ MODELS =====================================================
class Employee(models.Model):
    GENDER = (
        		('male','male'),
           ('female','female'),
        )
    NATIONALITY = (
        			('indian','indian'),
                ('other','other'),
                  )
    MARITAL = (
        		('single','single'),
           ('married','married'),
                ('divorced','divorced'),
                ('other','other'),
              )

    emp_id = models.AutoField
    emp_code = models.CharField(
        max_length=30,
        editable=True,
        unique=True,
        default=create_emp_code()
    )
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices = GENDER)
    marital_status = models.CharField(max_length=10, choices = MARITAL)
    nationality = models.CharField(max_length=10, choices = NATIONALITY)
    address =  models.TextField()
    zipcode = models.CharField(max_length=10)
    email = models.EmailField()
    mobile = models.CharField(max_length=12)

    designation = models.CharField(max_length=30)
    experience = models.FloatField()
    joining_dt = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Employee"
    
    def __str__(self):
        return self.name