from random import randint

from rest_framework.test import APIClient, APITestCase

from care.models import ReabilatationCenter
from users.models import ContactData, CustomUser


class CenterTests(APITestCase):
    data = {
        "name": "123",
        "contact_data": {"phone": "321", "city": "321", "address": "312"},
        "description": "string",
        "specialisation": "MEDICAL",
        "schedule": "string",
    }

    @classmethod
    def setUpTestData(cls):
        data = cls.data.copy()
        contact_data = data.pop("contact_data")
        contact = ContactData.objects.create(**contact_data)
        ReabilatationCenter.objects.create(contact_data=contact, **data)

    def test_create_center(self):
        url = "/api/v1/care/centers/"
        client = APIClient()
        response = client.post(url, self.data, format="json")
        response_data = response.json()
        data = self.data.copy()
        data["id"] = response_data["id"]
        data["contact_data"]["id"] = response_data["contact_data"]["id"]
        self.assertEqual(data, response_data)

    def test_update_center(self):
        url = "/api/v1/care/centers/"
        client = APIClient()
        data = self.data.copy()
        obj_id = client.post(url, data, format="json").json()["id"]
        data["name"] = "Название"
        data["contact_data"]["phone"] = "89999999"
        response = client.patch(url + str(obj_id) + "/", data, format="json").json()
        data["id"] = response["id"]
        data["contact_data"]["id"] = response["contact_data"]["id"]
        self.assertEqual(data, response)

    def test_rate_center(self):
        client = APIClient()
        sum_rating = 0
        for i in range(1, 11):
            username = "user{}@mail.com".format(i)
            CustomUser.objects.create_user(email=username, password="123qwe")
            client.login(username=username, password="123qwe")
            rating = randint(1, 5)
            sum_rating += rating
            client.post(
                "/api/v1/care/centers/1/rate/", {"rating": rating, "text": "text"}
            )
            client.logout()
        response = client.get("/api/v1/care/centers/").json()
        self.assertEqual(response["results"][0]["rating"], round(sum_rating / 10, 1))
