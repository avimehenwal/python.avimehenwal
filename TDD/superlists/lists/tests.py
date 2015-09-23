from django.test import TestCase

# Functional TC  -> from the point of view of user
# Unit Test Case -> from the point of view of developer

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1, 3)


