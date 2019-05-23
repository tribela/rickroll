from django.test import TestCase
from django.shortcuts import reverse

from .models import Link


class RickrollTest(TestCase):

    def setUp(self):
        Link.objects.create(
            id=1,
            title='test title',
            description='test description',
            destination='http://test.com',
        )

    def test_id_str(self):
        link = Link.objects.get(id=1)
        self.assertEqual(link.id_str, '2')

    def test_attributes(self):
        link = Link.objects.get(id=1)
        self.assertEqual(link.title, 'test title')
        self.assertEqual(link.description, 'test description')
        self.assertEqual(link.destination, 'http://test.com')

    def test_preview(self):
        link = Link.objects.get(id=1)
        url = reverse('preview', args=[link.id_str])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(link.destination, response.content.decode())
        self.assertIn(link.title, response.content.decode())
        self.assertIn(link.description, response.content.decode())

    def test_link_view(self):
        link = Link.objects.get(id=1)
        url = reverse('link_view', args=[link.id_str])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(link.destination, response.content.decode())
        self.assertIn(link.title, response.content.decode())
        self.assertIn(link.description, response.content.decode())

    def test_404(self):
        url_preview = reverse('preview', args=['00'])
        response = self.client.get(url_preview)
        self.assertEqual(response.status_code, 404)
