from django.test import TestCase, Client
from django.urls import reverse, resolve
from HIVCenter.views import show_homepage  
# Create your tests here.
class AppTest(TestCase):
    # --------------------- URL ---------------------------- #
    def test_show_homepage_url(self):
        url = reverse("hivcenter:show_homepage")
        self.assertEquals(resolve(url).func, show_homepage)
    # --------------------- Views ---------------------------- #
    def test_view_show_homepage(self):
        client = Client()
        response = client.get(reverse("hivcenter:show_homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage.html")