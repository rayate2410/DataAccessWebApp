from django.db import models
from django.contrib.auth.models import User

from time import time   

# Create your models here.

def get_upload_file_name(instance, filename):
    return 'upload/'+str(time()).replace('.','_')+"_"+filename

class TestCase(models.Model):
    'Employees Details are here'
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=200,default='NE')
    creation_date = models.DateField('Date added')
    screenshot = models.FileField(upload_to=get_upload_file_name)
    #created_by = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title