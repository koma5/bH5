from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Track

class ViewFunctionTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_dont_show_private_tracks_on_index_if_unauthenticated(self):

        name = 'testSecretTrack'

        user = User()
        user.save()

        track = Track(name=name, public=False, owner=user)
        track.save()

        url = reverse('tracks:index')
        response = self.client.get(url)

        #print(response.content)

        self.assertNotContains(response, name)

