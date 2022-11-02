from django.test import TestCase, Client, RequestFactory
from Blogpost.views import create_blogpost, delete_blogpost, show_blogpost, show_blogpost_by_id, show_blogpost_json, show_blogpost_json_by_id, show_user, update_blogpost
from Blogpost.models import BlogpostModel
from django.urls import reverse, resolve
from Authentication.models import User

# Create your tests here.
class AppTest(TestCase):
    # --------------------- URL ---------------------------- #
    def test_show_blogpost_url(self):
        url = reverse("blogpost:show_blogpost")
        self.assertEquals(resolve(url).func, show_blogpost)
    def test_show_user_url(self):
        url = reverse("blogpost:show_user", args=[1])
        self.assertEquals(resolve(url).func, show_user)
    def test_create_blogpost_url(self):
        url = reverse("blogpost:create_blogpost")
        self.assertEquals(resolve(url).func, create_blogpost)
    def test_show_blogpost_by_id_url(self):
        url = reverse("blogpost:show_blogpost_by_id", args = [1])
        self.assertEquals(resolve(url).func, show_blogpost_by_id) 
    def test_show_blogpost_json_url(self):
        url = reverse("blogpost:show_blogpost_json")
        self.assertEquals(resolve(url).func, show_blogpost_json)
    def test_show_blogpost_json_by_id_url(self):
        url = reverse("blogpost:show_blogpost_json_by_id", args = [1])
        self.assertEquals(resolve(url).func, show_blogpost_json_by_id) 
    def test_update_blogpost_url(self):
        url = reverse("blogpost:update_blogpost", args = [1])
        self.assertEquals(resolve(url).func, update_blogpost) 
    def test_delete_blogpost_url(self):
        url = reverse("blogpost:delete_blogpost", args = [1])
        self.assertEquals(resolve(url).func, delete_blogpost) 

    # --------------------- Views ---------------------------- #
    def test_view_show_blogpost(self):
        client = Client()
        response = client.get(reverse("blogpost:show_blogpost"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogpost.html")

    def test_view_show_user(self):
        client = Client()
        self.id = User.objects.create(
            username = "alvaro",
            password = "pbpkelasd",
            role = 1
        ).id

        response = client.get(reverse("blogpost:show_user",args = [self.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_show_blogpost_json(self):
        client = Client()
        response = client.get(reverse("blogpost:show_blogpost_json"))
        self.assertEqual(response.status_code, 200)

    def test_view_show_blogpost_json_by_id(self):
        client = Client()
        user = User.objects.create(
            username = "alvaro",
            password = "pbpkelasd",
            role = 1
        )
        item = BlogpostModel.objects.create(
            importance = "LW",
            user = user, 
            title = "Halo",
            opening = "Opening",
            main = "Main",
            closing = "Closing"
        )        
        response = client.get(reverse("blogpost:show_blogpost_json_by_id", args = [item.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_show_blogpost_by_id(self):
        client = Client()
        user = User.objects.create(
            username = "alvaro",
            password = "pbpkelasd",
            role = 1
        )
        self.id = BlogpostModel.objects.create(
            importance = "LW",
            user = user, 
            title = "Halo",
            opening = "Opening",
            main = "Main",
            closing = "Closing"
        ).id        

        response = client.get(reverse("blogpost:show_blogpost_by_id", args = [self.id]))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.request_factory = RequestFactory()
        self.user = User.objects.create_user(
        username='javed', email='javed@javed.com', password='pbpkelasd', role = 2)
        self.user2 = User.objects.create_user(
        username='javed2', email='javed2@javed.com', password='pbpkelasd', role = 1)

    def test_view_create_blogpost(self):
        client = Client()
        response = client.get(reverse("blogpost:create_blogpost"))
        self.assertEqual(response.status_code, 403)

    def test_view_create_blogpost_2(self):
        payload = {
            'title': 'my first question title',
            'opening': 'my first question',
            'main': 'my first question',
            'closing': 'first, question',
            'importance': "LW"
        }

        request = self.request_factory.post("/create/", payload)
        request.user = self.user
        response = create_blogpost(request)
        self.assertEqual(response.status_code, 200)

    def test_view_create_blogpost_3(self):
        
        payload = {
            'title': 'my first question title',
            'opening': 'my first question',
            'main': 'my first question',
            'closing': 'first, question',
            'importance': "LW"
        }

        request = self.request_factory.post("/create/", payload)
        request.user = self.user2
        response = create_blogpost(request)
        self.assertEqual(response.status_code, 403)

    def test_view_update_blogpost(self):
        client = Client()
        user = User.objects.create(
            username = "alvaro",
            password = "pbpkelasd",
            role = 1
        )
        self.id = BlogpostModel.objects.create(
            importance = "LW",
            user = user, 
            title = "Halo",
            opening = "Opening",
            main = "Main",
            closing = "Closing"
        ).id

        response = client.get(reverse("blogpost:update_blogpost", args = [self.id]))
        self.assertEqual(response.status_code, 403)

    # def test_view_update_blogpost_2(self):

    #     self.id = BlogpostModel.objects.create(
    #         importance = "LW",
    #         user = self.user, 
    #         title = "Halo",
    #         opening = "Opening",
    #         main = "Main",
    #         closing = "Closing"
    #     ).id        

    #     payload = {
    #         'title': 'my first question title',
    #         'opening': 'my first question',
    #         'main': 'my first question',
    #         'closing': 'first, question',
    #         'importance': "LW"
    #     }

    #     request = self.request_factory.put(f"/update/{self.id}/", payload)
    #     request.user = self.user
    #     request.method = "PUT"
    #     response = update_blogpost(request, self.id)
    #     self.assertEqual(response.status_code, 200)

    def test_view_update_blogpost_3(self):
        payload = {
            'title': 'my first question title',
            'opening': 'my first question',
            'main': 'my first question',
            'closing': 'first, question',
            'importance': "LW"
        }

        request = self.request_factory.post("/update/1/", payload)
        request.user = self.user2
        response = update_blogpost(request, 1)
        self.assertEqual(response.status_code, 403)

    def test_view_delete_blogpost(self):
        client = Client()
        user = User.objects.create(
            username = "alvaro",
            password = "pbpkelasd",
            role = 1
        )
        self.id = BlogpostModel.objects.create(
            importance = "LW",
            user = user, 
            title = "Halo",
            opening = "Opening",
            main = "Main",
            closing = "Closing"
        ).id        
        response = client.get(reverse("blogpost:delete_blogpost", args = [self.id]))
        self.assertEqual(response.status_code, 403)

    def test_view_delete_blogpost_2(self):
        self.id = BlogpostModel.objects.create(
            importance = "LW",
            user = self.user, 
            title = "Halo",
            opening = "Opening",
            main = "Main",
            closing = "Closing"
        ).id        

        request = self.request_factory.delete("/delete/1/")
        request.user = self.user
        request.method = "DELETE"
        response = delete_blogpost(request, 1)
        self.assertEqual(response.status_code, 200)

    # --------------------- Templates ---------------------------- #
    def test_blogpost_using_template(self):
        response = Client().get('/blogpost/')
        self.assertTemplateUsed(response, 'blogpost.html')
    def test_blogpost_id_using_template(self):
        user = User.objects.create(
            username = "alvaro",
            password = "pbpkelasd",
            role = 1
        )
        self.id = BlogpostModel.objects.create(
            importance = "LW",
            user = user, 
            title = "Halo",
            opening = "Opening",
            main = "Main",
            closing = "Closing"
        ).id
        response = Client().get(f'/blogpost/{self.id}/')
        self.assertTemplateUsed(response, 'blogpost_item.html')
        
    # --------------------- Model ---------------------------- #
    def test_model_blogpost(self):
        user = User.objects.create(
            username = "alvaro",
            password = "pbpkelasd",
            role = 1
        )

        item = BlogpostModel.objects.create(
            importance = "LW",
            user = user, 
            title = "Halo",
            opening = "Opening",
            main = "Main",
            closing = "Closing"
        )
        self.assertEqual(BlogpostModel.objects.get(title = "Halo").title, \
            "Halo")
        self.assertTrue(isinstance(item, BlogpostModel))