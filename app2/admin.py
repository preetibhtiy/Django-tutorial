from django.contrib import admin
#from.models import Students
#class Studentsdata(admin.ModelAdmin):
 #   list_display=['first_name','last_name','age']
#admin.site.register(Students,Studentsdata)
from.models import Employee
class Employeedata(admin.ModelAdmin):
    list_display=['eid','ename','econtact']
admin.site.register(Employee,Employeedata)