from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import UserRegisterView


class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)
        # assert resolve(url).func.view_class == UserRegisterView, "Incorrect class"
