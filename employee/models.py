from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    STATUS_CHOICES = [('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee} - {self.date}"


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    total_days = models.IntegerField()
    days_present = models.IntegerField()
    days_absent = models.IntegerField()
    salary_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee} - {self.month.strftime('%B %Y')}"
