import django_filters as df
from .models import Employee, Performance
from .models import Attendance  # if Attendance model is in employees app

class EmployeeFilter(df.FilterSet):
    date_of_joining_after = df.DateFilter(field_name="date_of_joining", lookup_expr="gte")
    date_of_joining_before = df.DateFilter(field_name="date_of_joining", lookup_expr="lte")
    class Meta:
        model = Employee
        fields = ["department", "date_of_joining_after", "date_of_joining_before"]

class AttendanceFilter(df.FilterSet):
    date_after = df.DateFilter(field_name="date", lookup_expr="gte")
    date_before = df.DateFilter(field_name="date", lookup_expr="lte")
    class Meta:
        model = Attendance
        fields = ["employee", "status", "date_after", "date_before"]

class PerformanceFilter(df.FilterSet):
    review_after = df.DateFilter(field_name="review_date", lookup_expr="gte")
    review_before = df.DateFilter(field_name="review_date", lookup_expr="lte")
    rating = df.NumberFilter(field_name="rating")
    class Meta:
        model = Performance
        fields = ["employee", "rating", "review_after", "review_before"]
