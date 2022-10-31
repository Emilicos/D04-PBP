import datetime
from django.test import TestCase
from django.urls import resolve, reverse
from Booking.models import Appointment

from Booking.views import add_booking, delete_booking, get_dokter_json, show_booking, show_json
from Authentication.models import User

# Create your tests here.
class BookingTest(TestCase):

    # --------------------- URL ---------------------------- #

    def test_show_booking_url(self):
        url = reverse("Booking:show_booking")
        self.assertEquals(resolve(url).func, show_booking)

    def test_show_json_url(self):
        url = reverse("Booking:show_json")
        self.assertEquals(resolve(url).func, show_json)

    def test_add_booking_url(self):
        url = reverse("Booking:add_booking")
        self.assertEquals(resolve(url).func, add_booking)

    def test_delete_booking_url(self):
        url = reverse("Booking:delete_booking", args = [1])
        self.assertEquals(resolve(url).func, delete_booking)

    def test_get_dokter_json_url(self):
        url = reverse("Booking:get_dokter_json")
        self.assertEquals(resolve(url).func, get_dokter_json)
    
    # --------------------- Views + Templates ---------------------------- #

    def test_view_show_booking_patient(self):
        self.user = User.objects.create(username='testpatient', first_name ='firstname', last_name='lastname', email='testpatient@gmail.com', role=1)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testpatient', password='password')
        response = self.client.get(reverse("Booking:show_booking"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='booking.html')

    def test_view_show_booking_doctor(self):
        self.user = User.objects.create(username='testdoctor', first_name ='firstname', last_name='lastname', email='testdoctorgmail.com', role=2)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testdoctor', password='password')
        response = self.client.get(reverse("Booking:show_booking"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='doctor.html')

    def test_view_show_json(self):
        self.user = User.objects.create(username='testuser', first_name ='firstname', last_name='lastname', email='testpatient@gmail.com', role=1)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse("Booking:show_json"))
        self.assertEqual(response.status_code, 200)

    def test_view_get_dokter_json(self):
        self.user = User.objects.create(username='testuser', first_name ='firstname', last_name='last_name', email='testuser@gmail.com', role=1)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse("Booking:get_dokter_json"))
        self.assertEqual(response.status_code, 200)

    def test_views_add_booking(self):
        self.user = User.objects.create(username='testuser', first_name ='firstname', last_name='lastname', email='testuser@gmail.com', role=1)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse("Booking:add_booking"), {'user' : self.user, 'date' : "2020-10-10", 'time' : "00:00", 'doctor' : "testdoctor"})
        self.assertEqual(response.status_code, 200)

    def test_views_delete_booking(self):
        self.user = User.objects.create(username='testuser', first_name ='firstname', last_name='lastname', email='testuser@gmail.com', role=1)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testuser', password='password')
        self.appointment = Appointment.objects.create(user = self.user, date = "2020-10-10", time = "00:00", doctor = "testdoctor")
        self.appointment.save()
        response = self.client.delete(reverse("Booking:delete_booking", args = {self.appointment.pk}))
        self.assertEqual(response.status_code, 200)

    # --------------------- Model ---------------------------- #

    def test_model_blogpost(self):
        patient = User.objects.create(
            username = "testpatient",
            password = "password",
            role = 1
        )

        item = Appointment.objects.create(
            user = patient, 
            date = "2020-10-10",
            time = "00:00",
            doctor = "testdoctor"
        )

        self.assertEqual(Appointment.objects.get(user = patient).user, patient)
        self.assertEqual(Appointment.objects.get(date = datetime.date(2020, 10, 10)).date, datetime.date(2020, 10, 10))
        self.assertEqual(Appointment.objects.get(time = datetime.time(0, 0)).time, datetime.time(0, 0))
        self.assertEqual(Appointment.objects.get(doctor = "testdoctor").doctor, "testdoctor")

        self.assertTrue(isinstance(item, Appointment))