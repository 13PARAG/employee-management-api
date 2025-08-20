from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employees.views import DepartmentViewSet, EmployeeViewSet, PerformanceViewSet, AttendanceViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'attendances', AttendanceViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="API for managing employees, attendance, and performance",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
