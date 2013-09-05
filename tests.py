from django.test import TestCase

from gctest.models import App, Build

class AppTests(TestCase):
    def current_build(self):
        """ 
        Tests if the current build is marked as current.
        """
        
