from random import randint

from django.utils import timezone
from rest_framework.test import APIClient, APITestCase

from care.models import Event, ReabilatationCenter
from users.models import ContactData, CustomUser


class CenterTests(APITestCase):
    center_data = {
        "name": "123",
        "contact_data": {"phone": "321", "city": "321", "address": "312"},
        "description": "string",
        "specialisation": "MEDICAL",
        "schedule": "string",
    }
    event_data = {
        "contact_data": {"phone": "321", "city": "321", "address": "312"},
        "name": "123",
        "place": "123",
        "start_date": timezone.now(),
    }

    @classmethod
    def setUpTestData(cls):
        center_data = cls.center_data.copy()
        contact_data = center_data.pop("contact_data")
        contact = ContactData.objects.create(**contact_data)
        ReabilatationCenter.objects.create(contact_data=contact, **center_data)
        event_data = cls.event_data.copy()
        contact_data = event_data.pop("contact_data")
        contact = ContactData.objects.create(**contact_data)
        Event.objects.create(contact_data=contact, **event_data)

    def test_create_center(self):
        url = "/api/v1/care/centers/"
        client = APIClient()
        response = client.post(url, self.center_data, format="json")
        response_data = response.json()
        center_data = self.center_data.copy()
        center_data["id"] = response_data["id"]
        center_data["contact_data"]["id"] = response_data["contact_data"]["id"]
        self.assertEqual(center_data, response_data)

    def test_update_center(self):
        url = "/api/v1/care/centers/"
        client = APIClient()
        center_data = self.center_data.copy()
        obj_id = client.post(url, center_data, format="json").json()["id"]
        center_data["name"] = "Название"
        center_data["contact_data"]["phone"] = "89999999"
        response_data = client.patch(
            url + str(obj_id) + "/", center_data, format="json"
        ).json()
        center_data["id"] = response_data["id"]
        center_data["contact_data"]["id"] = response_data["contact_data"]["id"]
        self.assertEqual(center_data, response_data)

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

    def test_create_event(self):
        url = "/api/v1/care/events/"
        client = APIClient()
        response = client.post(url, self.event_data, format="json")
        response_data = response.json()
        event_data = self.event_data.copy()
        event_data["id"] = response_data["id"]
        event_data["start_date"] = response_data["start_date"]
        event_data["contact_data"]["id"] = response_data["contact_data"]["id"]
        self.assertEqual(event_data, response_data)

    def test_update_event(self):
        url = "/api/v1/care/events/"
        client = APIClient()
        event_data = self.event_data.copy()
        obj_id = client.post(url, event_data, format="json").json()["id"]
        event_data["name"] = "Название"
        event_data["contact_data"]["phone"] = "89999999"
        response_data = client.patch(
            url + str(obj_id) + "/", event_data, format="json"
        ).json()
        event_data["id"] = response_data["id"]
        event_data["start_date"] = response_data["start_date"]
        event_data["contact_data"]["id"] = response_data["contact_data"]["id"]
        self.assertEqual(event_data, response_data)

    def test_register_event(self):
        client = APIClient()
        username = "user1@mail.com"
        event_data = self.event_data.copy()
        CustomUser.objects.create_user(email=username, password="123qwe")
        client.login(username=username, password="123qwe")
        response_data = client.post("/api/v1/care/events/1/register/").json()
        event_data["id"] = response_data["event"]["id"]
        event_data["start_date"] = response_data["event"]["start_date"]
        event_data["contact_data"]["id"] = response_data["event"]["contact_data"]["id"]
        self.assertEqual(response_data["user"]["email"], username)
        self.assertEqual(response_data["event"], event_data)
