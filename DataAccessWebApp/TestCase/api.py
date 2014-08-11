from tastypie.resources import ModelResource
from models import TestCase
from tastypie.constants import ALL

class TestCaseResource(ModelResource):
    class Meta:
        queryset = TestCase.objects.all()
        resource_name = 'tc'
        filtering = {'title', ALL } 