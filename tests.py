"""Integration Testing Flask app"""

from server import app

from unittest import TestCase

# To test:
# python tests.py

# Coverage config file -- .coveragerc

# Coverage:
# coverage run tests.py
# coverage report -m

# HTML coverage report:
# coverage run tests.py
# coverage html


class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests in the console
        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage."""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('<div class="jumbotron">', result.data)
        self.assertIn('<h1>Tweegle</h1>', result.data)

    def test_search(self):
        """Test search results page."""

        result = self.client.get('/search?q=food')
        self.assertEqual(result.status_code, 200)
        self.assertNotIn('<div class="jumbotron">', result.data)
        self.assertIn('<div class="navbar-header">', result.data)
        self.assertIn('left-col', result.data)
        self.assertIn('right-col', result.data)
        self.assertIn('Hashtags', result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()