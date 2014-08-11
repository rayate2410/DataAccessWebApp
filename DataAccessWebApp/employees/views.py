from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

import models
from employees.models import EmployeeDetails

# Create your views here.

def index(request):
   
    if "last_viewed" in request.COOKIES:
        emp = EmployeeDetails.objects.get(id=request.COOKIES["last_viewed"])
        response = render_to_response("employee_home.html", {"emp":emp})
    else:
        response = render_to_response("employee_home.html", {"emp":"None"})

            
    return response

def template_example(request):
    emp = EmployeeDetails.objects.get(id=2)
       
    name = emp.emp_name
    roll_no = emp.emp_roll_no
    template = get_template("simple_template.html")
    html = template.render(Context({"name": name, "roll_no": roll_no}))
    return HttpResponse(html)

def rendertoresponse(request):
    emp = EmployeeDetails.objects.get(id=1)
       
    name = emp.emp_name
    roll_no = emp.emp_roll_no
    return render_to_response("simple_template.html", {"name": name, "roll_no": roll_no})

def get_Employee_details(request):
    
    emp_id = request.GET.get('id')
    
    try:
        emp = EmployeeDetails.objects.get(id=emp_id)
        response = render_to_response("employee_detail.html", {"emp" : emp})
        response.set_cookie("last_viewed", emp.id)
    except Exception:
        response = render_to_response("no_employee.html", {"emp" : emp_id})
        
        
    
    return response
    


def get_all(request):
    '''
    employees = EmployeeDetails.objects.all()
    json_resp = {}
    json_resp["count"] = employees.count()
    print employees.count()
    count = 0
    for emp in employees:
        #json_resp[0]["emp_name"] = emp.emp_name
        print emp.emp_name
        count = count + 1
    '''
    return render_to_response("employees.html", {"employees" : EmployeeDetails.objects.all()})