from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

"""        
Functional TC  -> from the point of view of user
Unit Test Case -> from the point of view of developer, logic, flow, configurations and not constrains
"""

#class SmokeTest(TestCase):
#
#    def test_bad_maths(self):
#        self.assertEqual(1+1, 3)


class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        print(found)
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.asserEqual(response.content.decode(), expected_html)

