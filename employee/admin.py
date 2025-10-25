from django.contrib import admin
from .models import Employee, Attendance, Payroll

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','designation','salary')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee','date','status')
    list_filter = ('status','date')

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee','month','days_present','days_absent','salary_paid')
    list_filter = ('month',)
