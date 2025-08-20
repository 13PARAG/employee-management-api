from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from employees.models import Department, Employee
from rest_framework import status

class AuthenticatedAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="tester", password="pass12345")
        
        # Obtain JWT token for the user
        resp = self.client.post(
            reverse("token_obtain_pair"), 
            {"username": "tester", "password": "pass12345"},
            format="json"
        )
        self.token = resp.data["access"]
        
        # Add JWT token to headers for authenticated requests
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        
        # Create a test department and employee
        self.dept = Department.objects.create(name="IT")
        self.emp = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            date_of_joining="2024-01-01",
            department=self.dept
        )

    def test_list_employees(self):
        # Test fetching employees list (authenticated)
        r = self.client.get("/api/employees/")
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(r.data["results"])  # Check paginated results

    def test_filter_by_department(self):
        # Test filtering employees by department
        r = self.client.get(f"/api/employees/?department={self.dept.id}")
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(r.data["results"]), 1)


class UnauthenticatedAPITests(APITestCase):
    def test_requires_auth(self):
        # Test that authentication is required
        r = self.client.get("/api/employees/")
        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)
