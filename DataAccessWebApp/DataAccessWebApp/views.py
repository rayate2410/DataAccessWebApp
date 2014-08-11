'''
Created on Jul 30, 2014

@author: rayy
'''
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from employees.models import EmployeeDetails
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from forms import MyRegistrationForm, AddTestCase


def index(request):
    emp = EmployeeDetails.objects.all()
    #print emp.count()
    return render_to_response("home.html")

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)

def auth_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user_obj = auth.authenticate(username = username, password = password)
    
    if user_obj is not None:
        auth.login(request, user_obj)
        return HttpResponseRedirect("/profile")
    else:
        return HttpResponseRedirect("/invalid")

def profile(request):
    if request.user.is_authenticated():
        #username = request.user.username
        return render_to_response("profile.html", {"logged_in": request.user} )
    else:
        return HttpResponseRedirect("/invalid")
    

def invalid(request):
    return render_to_response("invalid.html")

def logout(request):
    auth.logout(request)
    return render_to_response("logout.html")

def register_view(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            print "form is valid"
            
            form.save()
            return HttpResponseRedirect('/registered')
        else:
            print form.error_messages
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['registration_form'] = form
    
    return render_to_response('register.html', args)

def registered_view(request):
    return render_to_response("registered.html")




