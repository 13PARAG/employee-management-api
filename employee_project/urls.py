from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView

# App views
from employees.views import (
    DepartmentViewSet,
    EmployeeViewSet,
    PerformanceViewSet,
    AttendanceViewSet,
    EmployeesPerDepartment,
    MonthlyAttendance,
)

# Swagger/OpenAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# DRF router
router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'attendances', AttendanceViewSet)

# Swagger schema config
schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version="v1",
        description="API for managing employees, departments, performance and attendance.",
        contact=openapi.Contact(email="your@email.com"),  # optional
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Main API
    path('api/', include(router.urls)),

    # Analytics endpoints
    path('api/analytics/employees-per-department/', EmployeesPerDepartment.as_view()),
    path('api/analytics/monthly-attendance/', MonthlyAttendance.as_view()),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger/OpenAPI docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Charts UI (uses `charts.html`)
    path('charts/', TemplateView.as_view(template_name="charts.html")),
]
