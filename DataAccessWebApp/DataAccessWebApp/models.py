from django.db import models
from django.contrib.auth.models import User


class TestCase(models.Model):
    'Employees Details are here'
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=200,default='NE')
    creation_date = models.DateField('Date added')
    created_by = models.ForeignKey(User)
    
    
    def __unicode__(self):
        return self.title