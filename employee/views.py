from django.shortcuts import render, redirect
from .models import Employee, Attendance, Payroll
from .forms import EmployeeForm, AttendanceForm
from django.http import HttpResponse
from datetime import date
import xlsxwriter
from reportlab.pdfgen import canvas

def dashboard(request):
    total_employees = Employee.objects.count()
    total_attendance = Attendance.objects.count()
    total_payroll = Payroll.objects.count()
    return render(request, 'employee/dashboard.html', {
        'total_employees': total_employees,
        'total_attendance': total_attendance,
        'total_payroll': total_payroll,
    })

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})

def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'employee/attendance_list.html', {'attendance': attendance})

def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'employee/payroll_list.html', {'payrolls': payrolls})

# PDF Export
def export_payroll_pdf(request, payroll_id):
    payroll = Payroll.objects.get(id=payroll_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="payroll_{payroll.id}.pdf"'
    c = canvas.Canvas(response)
    c.drawString(100, 800, f"Payroll for {payroll.employee}")
    c.drawString(100, 780, f"Month: {payroll.month.strftime('%B %Y')}")
    c.drawString(100, 760, f"Days Present: {payroll.days_present}")
    c.drawString(100, 740, f"Days Absent: {payroll.days_absent}")
    c.drawString(100, 720, f"Salary Paid: ₹{payroll.salary_paid}")
    c.showPage()
    c.save()
    return response

# Excel Export
def export_payroll_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="payroll.xlsx"'
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    worksheet = workbook.add_worksheet('Payroll')
    worksheet.write(0,0,'Employee')
    worksheet.write(0,1,'Month')
    worksheet.write(0,2,'Days Present')
    worksheet.write(0,3,'Days Absent')
    worksheet.write(0,4,'Salary Paid')
    payrolls = Payroll.objects.all()
    row=1
    for p in payrolls:
        worksheet.write(row,0,str(p.employee))
        worksheet.write(row,1,p.month.strftime('%B %Y'))
        worksheet.write(row,2,p.days_present)
        worksheet.write(row,3,p.days_absent)
        worksheet.write(row,4,float(p.salary_paid))
        row+=1
    workbook.close()
    return response

