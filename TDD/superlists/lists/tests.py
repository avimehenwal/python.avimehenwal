from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

        
# Functional TC  -> from the point of view of user
# Unit Test Case -> from the point of view of developer


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1, 3)


class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        print(found)
        self.assertEqual(found.func, home_page)
