from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from items.models import Item


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item = Item.objects.create(
            name="rice",
            price="10.20",
            description="1KG",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("item_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Item.objects.count(), 1)
        self.assertContains(response, self.item)
