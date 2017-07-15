import json
from django.test import TestCase
from .models import UserProxy


class UserTestCase(TestCase):
    fixtures = [
        'test_users',
    ]

    def setUp(self):
        self.admin = UserProxy.objects.get(username='admin')
        self.editor = UserProxy.objects.get(username='editor')
        self.guest = UserProxy.objects.get(username='guest')

    def login(self, username, password=None):
        credentials = {'username': username, 'password': password or username}
        return self.client.login(**credentials)  # True or False

    def get_json(self, api, expected=200):
        r = self.client.get(api)
        self.assertEqual(r.status_code, expected)
        return json.loads(r.content.decode('utf-8'))

    def post_json(self, api, data, expected=201):
        r = self.client.post(api, json.dumps(data), content_type='application/json')
        self.assertEqual(r.status_code, expected)
        return json.loads(r.content.decode('utf-8'))
