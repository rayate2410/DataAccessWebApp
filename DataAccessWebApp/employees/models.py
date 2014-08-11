from django.db import models


# Create your models here.

class EmployeeDetails(models.Model):
    'Employees Details are here'
    emp_name = models.CharField(max_length=200)
    emp_roll_no = models.IntegerField()
    emp_salary = models.IntegerField()
    emp_post = models.CharField(max_length=200)
    emp_profile = models.TextField()
    emp_join_date = models.DateField('date joined')
    
    def __unicode__(self):
        return self.emp_name
    