from django.test import TestCase
from unittest.mock import patch

from .models import Movie

REQUESTS_GET = 'omdb.requests.get'

def mocked_requests_get(data):

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(data, 201)

def test_save_movie(self, mock_requests):
        #Sprawdzenie czy zapostowanie filmy zapisuje do databazy#
        self.assertEqual(Movie.objects.count(), 0)
        resp = self.client.post('/movies/', {'title': 'Django Unchained'})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Movie.objects.count(), 1)


def test_get_movie(self):
    #Sprawdzenie czy film jest uzskiwany w GET#
        self.client.post('/movies/', {'title': 'Django Unchained'})
        resp = self.client.get('/movies/')
        self.assertEqual('Django Unchained', resp.data['results'][0]['title'])

def test_filter_movie(self):
        # Sprawdzenie filtrowania #
        with patch(REQUESTS_GET, return_value=mocked_requests_get(data={'Title': 'Django Unchained'})):
            self.client.post('/movies/', {'title': 'Django Unchained'})
        with patch(REQUESTS_GET, return_value=mocked_requests_get(data={'Title': 'Inception'})):
            self.client.post('/movies/', {'title': 'Inception'})

        resp = self.client.get('/movies/?search=Inception')
        self.assertEqual(len(resp.data['results']), 1)
        self.assertEqual('Inception', resp.data['results'][0]['title'])


class TestCommentsRestApi(TestCase):
    # Test komentarzy #

    def test_add_comments(self):
        #Test POST czy POST komentarze są dodawane do databazy#
        with patch(REQUESTS_GET, return_value=mocked_requests_get(data={'Title': 'Harry Potter'})):
            self.client.post('/movies/', {'title': 'Inception'})
        self.client.post('/comments/', {'comment': 'some long comment', 'author': 'author1', 'movie': 1})
        resp = self.client.get('/comments/')
        self.assertEqual(resp.data['results'][0]['author'], 'author1')
        self.assertEqual(resp.data['results'][0]['comment'], 'some long comment')
