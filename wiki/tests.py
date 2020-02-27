# wiki/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page

class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
            """ Tests the slug generated when saving a Page. """
            # Author is a required field in our model.
            # Create a user for this test and save it to the test database.
            user = User.objects.create()

            # Create and save a new page to the test database.
            page = Page.objects.create(title="My Test Page", content="test", author=user)
            page.save()

            # Make sure the slug that was generated in Page.save()
            # matches what we think it should be.
            self.assertEqual(page.slug, "my-test-page")

class PageListViewTests(TestCase):
    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="test", author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Page: My Test Page>', '<Page: Another Test Page>'],
            ordered=False
        )
    
    def test_single_page(self):
        user = User.objects.create()

        Page.objects.create(title='Test Page', content='test', author=user)

        response = self.client.get('/test-page/')

        self.assertEqual(response.status_code, 200)

        response = response.context['page']
        
        self.assertEqual(str(response), 'Test Page')
    
    def test_view_form_page(self):
        response = self.client.get('/create/')
        # Check request succeeded
        self.assertEqual(response.status_code, 200)
        # Check content
        self.assertIn(b'Title of your page', response.content)
    
    def test_create_page(self):
        user = User.objects.create()

        data = {
            'title': 'Test Page',
            'content': 'a test page',
            'author': user.id
        }

        response = self.client.post('/create/', data=data)
        self.assertEqual(response.status_code, 302)

        item = Page.objects.get(title='Test Page')
        self.assertEqual(item.title, 'Test Page')