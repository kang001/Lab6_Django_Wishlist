from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Place
# Create your tests here.

class TestViewHomePageIsEmptyList(TestCase):
    def test_load_home_page_shpws_empty_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places']) #empty lists are false

class TestWishList(TestCase):
    fixtures = ['test_places']

    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        data_rendered = list(response.context['places'])
        data_expected = list(Place.objects.filter(visited=False))

        self.assertCountEqual(data_rendered, data_expected)
        #checks to see if two lists have the same data
