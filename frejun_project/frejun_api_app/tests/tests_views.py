import json
from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from frejun_api_app.models import Account, PhoneNumber


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.inbound_url = reverse('inbound')
        self.account1 = Account.objects.create(auth_id="6DLH8A25XZ", username="plivo5")
        self.account2 = Account.objects.create(auth_id="54P2EOKQ47", username="plivo2")
        self.ph1 = PhoneNumber.objects.create(number="61871112931", account=self.account1)
        self.ph2 = PhoneNumber.objects.create(number="61871112939", account=self.account1)
        self.ph3 = PhoneNumber.objects.create(number="441224459660", account=self.account2)
        self.ph4 = PhoneNumber.objects.create(number="441873440028", account=self.account2)
        
        

    def test_if_authenticated_POST(self):
        username = self.account1.username
        auth_id = self.account1.auth_id
        response = self.client.post(
            self.inbound_url, {'username': username, 'auth_id': auth_id})
        self.assertEquals(response.status_code, 200)
