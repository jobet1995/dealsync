from typing import Any
from django.test import TestCase
from home.models import HomePage

from wagtail.models import Page, Site


class HomeSetUpTests(TestCase):
    """
    Tests for basic page structure setup and HomePage creation.
    """

    def test_root_create(self):
        root_page = Page.objects.get(pk=1)
        self.assertIsNotNone(root_page)

    def test_homepage_create(self):
        root_page = Page.objects.get(pk=1)
        homepage = HomePage(title="Home")
        root_page.add_child(instance=homepage)
        self.assertTrue(HomePage.objects.filter(title="Home").exists())


class HomeTests(TestCase):
    """
    Tests for homepage functionality and rendering.
    """

    def setUp(self):
        """
        Create a homepage instance for testing.
        """
        # Delete any existing homepage
        HomePage.objects.all().delete()
        
        root_page = Page.objects.get(pk=1)
        self.homepage = HomePage(title="Home", slug="home")
        root_page.add_child(instance=self.homepage)
        
        # Delete any existing sites and create a new one with the homepage as the root
        Site.objects.all().delete()
        Site.objects.create(
            hostname='localhost',
            port=80,
            root_page=self.homepage,
            is_default_site=True
        )

    def test_homepage_loads(self):
        response: Any = self.client.get('/')
        # Check that we get a successful response
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_welcome_text(self):
        response: Any = self.client.get('/')
        # Check that we get a successful response
        self.assertEqual(response.status_code, 200)
        # Check that the welcome page content is present
        self.assertContains(response, "Welcome to your new Wagtail site!")