from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import home, sign_up, login
from booking.views import logout_view, admin_login, feedback, profile
from booking.views import booking_form, BookingDetailView
from booking.models import Booking, Profile


class TestUrls(SimpleTestCase):
    """
    To test urls.
    """
    def test_home_url_is_resolves(self):
        """ To test the home url """
        url = reverse('home')
        response = self.client.get('')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
        self.assertTemplateUsed(response, 'index.html')


    def test_sign_up_url_is_resolves(self):
        """ To test the signup url """
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, sign_up)


    def test_login_url_is_resolves(self):
        """ To test the login url """
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)
       

    def test_logout_url_is_resolves(self):
        """ To test the logout url """
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_view)


    def test_profile_url_is_resolves(self):
        """ To test the profile url """
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)
       

    def test_booking_form_url_is_resolves(self):
        """ To test the booking form url """
        url = reverse('booking_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, booking_form)


# class TestBookingModels(TestCase):
#     """
#     To test the booking models.
#     """
#     def test_booking_model(self):
#         booking = Booking.objects.create(
#             session_name='Beginner',
#         )

#         self.assertEquals(booking.session_name, 'Beginner')
      

