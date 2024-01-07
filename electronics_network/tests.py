from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from electronics_network.models import Company
from users.models import User


class CompanyTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
            is_active=True,
        )
        self.user.set_password('12345')
        self.user.save()
        self.client = APIClient()

        self.company = Company.objects.create(
            name='test_name',
            debt=0,
            company_type='factory'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_company(self):
        """ Тест создания компании """

        data = {
            "email": "test@test.com",
            "password": "12345"
        }
        user_response = self.client.post(
            "/api/token/",
            data=data
        )

        token = user_response.data['access']

        data = {
            'name': 'test_create',
            'supplier': 1,
            'company_type': 'retail_network',

        }
        response = self.client.post(
            "/api/company/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Company.objects.all().count() > 1)
        self.assertEqual(response.json()['supplier'], 1)
        self.assertEqual(str(Company.objects.get(pk=2)), "test_create")

    def test_list_companies(self):
        """ Тест вывода списка компаний """

        Company.objects.create(name="Test list", company_type="retail_network")
        response = self.client.get(
            '/api/companies/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_company(self):
        """ Тест обновления и удаления компании, debt не изменяется через
        API. """

        data = {
            "email": "test@test.com",
            "password": "12345"
        }
        user_response = self.client.post(
            "/api/token/",
            data=data
        )
        token = user_response.data['access']

        Company.objects.create(name="Test_1", debt=1000,
                               company_type="retail_network")

        data = {
            "name": "Test_update",
            "debt": 15,
        }

        response = self.client.patch(
            '/api/company/update/6/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.get(pk=6).debt, 1000)
        self.assertEqual(Company.objects.get(pk=6).name, 'Test_update')

        self.client.delete(
            '/api/company/delete/6/',
            headers={"Authorization": f"Bearer {token}"}
        )

        queryset = Company.objects.all()
        self.assertTrue(len(queryset) == 1)

    def tearDown(self):
        User.objects.all().delete()
        Company.objects.all().delete()
        return super().tearDown()
