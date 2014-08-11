from django.shortcuts import render_to_response
from forms import AddTestCase
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from models import TestCase
# Create your views here.
def add_testcase(request):
    if request.method == 'POST':
        form = AddTestCase(request.POST, request.FILES)
        if form.is_valid():
            print "form is valid"
            
            form.save()
            return HttpResponseRedirect('/testcase/added')
        else:
            print form
        
    else:
        form = AddTestCase()
    args = {}
    args.update(csrf(request))
    
    args['testcase_form'] = form
    
    return render_to_response('add_testcase.html', args)

def index(request):
    return render_to_response('testcase_home.html')

def added(request):
    return render_to_response('testcase_added.html')

def all(request):
    testcases = TestCase.objects.all()
    return render_to_response('testcase.html', {'testcases': testcases})

def get_tc_detail(request,tc_id=1):
    tc = TestCase.objects.get(id=tc_id)
    return render_to_response('testcase_detail.html', {'tc': tc})

def change_status(request, tc_id):
    status = request.GET.get('status')
       
    tc = TestCase.objects.get(id = tc_id)
    tc.status = status
    tc.save()
    
    return HttpResponseRedirect('/testcase/get/'+tc_id)


def search_tc(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
        
    tc = TestCase.objects.filter(title__contains=search_text)
    
    return render_to_response('tc_search.html', {'tc':tc})

def search(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('search.html', args)
    

