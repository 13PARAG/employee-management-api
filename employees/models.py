from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_joining = models.DateField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="employees"
    )

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_attendance')

    date = models.DateField()
    status = models.CharField(max_length=10, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave')
    ])

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    rating = models.IntegerField()    
    comments = models.TextField(default="")     # Correct syntax here

    def __str__(self):
        return f"{self.employee.name} - {self.rating}"
