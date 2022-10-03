from django.test import TestCase
from django.utils import timezone
from pages.models import Contact


class ContactTest(TestCase):
    """ Testing a Contact """
    def create_contact(
        self,
        name='bob',
        email='bob@bob.com',
        body='hello there!'
    ):

        return Contact.objects.create(
            name=name,
            email=email,
            created_on=timezone.now()
            )

    def test_contact_creation(self):
        test = self.create_contact()
        
        self.assertTrue(isinstance(test, Contact))
        self.assertEqual(test.__str__(), test.name)
    