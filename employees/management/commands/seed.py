from django.core.management.base import BaseCommand
from employees.models import Department, Employee, Attendance, Performance
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        # Create Departments
        departments = []
        for name in ['HR', 'Engineering', 'Marketing', 'Sales']:
            dept, _ = Department.objects.get_or_create(name=name)
            departments.append(dept)

        # Create Employees
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                department=random.choice(departments),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today')
            )

            # Attendance
            for _ in range(10):  # 10 days
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent', 'Leave'])
                )

            # Performance
            Performance.objects.create(
                employee=emp,
                review_date=fake.date_this_year(),
                rating=random.randint(1, 10),
                comments=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))

