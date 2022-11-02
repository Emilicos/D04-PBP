from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from Experience.views import create_experience_ajax, show_experience, show_experience_detail, show_experience_json
from Experience.models import Experience
from django.urls import reverse, resolve
from Authentication.models import User
import datetime
# Create your tests here.
class AppTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', first_name ='firstname', last_name='last_name', email='testuser@gmail.com', role=2)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testuser', password='password')
    # --------------------- URL ---------------------------- #
    def test_show_experience_url(self):
        url = reverse("Experience:show_experience")
        self.assertEquals(resolve(url).func, show_experience)
    # def test_show_experience_detail_url(self):
    #     url = reverse("Experience:show_experience_detail")
    #     self.assertEquals(resolve(url).func, show_experience_detail)
    def test_show_experience_json_url(self):
        url = reverse("Experience:show_experience_json")
        self.assertEquals(resolve(url).func, show_experience_json)
    def test_create_experience_ajax_url(self):
        url = reverse("Experience:create_experience_ajax")
        self.assertEquals(resolve(url).func, create_experience_ajax) 
     

    # --------------------- Views ---------------------------- #
    # def test_view_create_experience_ajax(self):
    #     self.client = Client()
    #     response = self.client.get(reverse("Experience:create_experience_ajax"))
    #     self.assertEqual(response.status_code, 200)

    def test_view_show_experience(self):
        self.client = Client()
        response = self.client.get(reverse("Experience:show_experience"))
        self.assertEqual(response.status_code, 200)

    # def test_view_show_experience_detail(self):
    #     self.client = Client()
    #     response = self.client.get(reverse("Experience:show_experience_detail") , 1)
    #     self.assertEqual(response.status_code, 200)

    def test_view_show_experience_json(self):
        self.client = Client()
        response = self.client.get(reverse('Experience:show_experience_json'))
        self.assertEqual(response.status_code, 200)
        
    
        
    # --------------------- Model ---------------------------- #
    def test_model_blogpost(self):
        user = User.objects.create(
            username = "carlene",
            password = "pbpkelasd",
            role = 1
        )

        item = Experience.objects.create(
            user = user, 
            username=user.username,
            title = "Halo",
            posted = datetime.datetime.now(),
            preview = "hi",
            experience = "hiiiiiiii"
        )
        self.assertEqual(Experience.objects.get(title = "Halo").title, \
            "Halo")
        self.assertTrue(isinstance(item, Experience))