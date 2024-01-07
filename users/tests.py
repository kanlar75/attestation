from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from electronics_network.models import Company
from users.models import User


class CompanyTestCase(APITestCase):

    def setUp(self):

        self.client = APIClient()

    def test_create(self):

        data = {
            'email': 'test@test.com',
            'password': '12312313A'
        }

        response = self.client.post(
            "/api/users/",
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



