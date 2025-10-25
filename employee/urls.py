from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('payroll/', views.payroll_list, name='payroll_list'),
    path('payroll/<int:payroll_id>/pdf/', views.export_payroll_pdf, name='export_payroll_pdf'),
    path('payroll/excel/', views.export_payroll_excel, name='export_payroll_excel'),
]
