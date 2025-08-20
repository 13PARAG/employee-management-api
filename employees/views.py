from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly  # Import the custom permission

from .models import Department, Employee, Performance, Attendance
from .serializers import DepartmentSerializer, EmployeeSerializer, PerformanceSerializer, AttendanceSerializer
from .filters import EmployeeFilter, AttendanceFilter, PerformanceFilter

# --- Standard ViewSets ---

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by("id")
    serializer_class = DepartmentSerializer
    search_fields = ["name"]
    ordering_fields = ["name", "id"]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]  # Added permissions

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related("department").all().order_by("id")
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter
    search_fields = ["name", "email", "phone_number", "department__name"]
    ordering_fields = ["date_of_joining", "name", "id"]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]  # Added permissions

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related("employee").all().order_by("id")
    serializer_class = AttendanceSerializer
    filterset_class = AttendanceFilter
    search_fields = ["employee__name", "status"]
    ordering_fields = ["date", "id"]
    # You can add permissions here later if needed

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.select_related("employee").all().order_by("id")
    serializer_class = PerformanceSerializer
    filterset_class = PerformanceFilter
    search_fields = ["employee__name"]
    ordering_fields = ["rating", "review_date", "id"]
    # You can add permissions here later if needed

# --- Analytics Endpoints ---

class EmployeesPerDepartment(APIView):
    def get(self, request):
        data = (
            Department.objects
            .annotate(total=Count("employees"))
            .values("name", "total")
            .order_by("name")
        )
        return Response(list(data))

class MonthlyAttendance(APIView):
    def get(self, request):
        qs = (
            Attendance.objects
            .annotate(month=TruncMonth("date"))
            .values("month", "status")
            .annotate(total=Count("id"))
            .order_by("month", "status")
        )

        # Reshape data for Chart.js
        months = sorted({str(i["month"])[:7] for i in qs})  # YYYY-MM
        statuses = sorted({i["status"] for i in qs})
        matrix = {s: {m: 0 for m in months} for s in statuses}
        for row in qs:
            m = str(row["month"])[:7]
            matrix[row["status"]][m] = row["total"]

        out = {
            "labels": months,
            "datasets": [
                {"label": s, "data": [matrix[s][m] for m in months]}
                for s in statuses
            ]
        }
        return Response(out)
