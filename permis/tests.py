from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.urls.base import resolve

from .forms import AddBookForm
from .models import Catalog
from .views import home


class CatalogViewTests(TestCase):
    """    Тест для представлений    """
    def test_book_list_view(self):

        Book_1 = Catalog.objects.create(
            title='Django for Beginners (2018)',
            ISBN='978-1-60309-0',
            author='John Doe',
            price=9.99,
            availability=True
        )

        Book_2 = Catalog.objects.create(
            title='Django for Professionals (2020)',
            ISBN='978-1-60309-3',
            author='Mary Doe',
            price=11.99,
            availability=False
        )

        response = self.client.get(reverse('permis:home'))

        self.assertIn('Django for Professionals (2020)', response.content.decode())
        self.assertIn('John Doe', response.content.decode())
        self.assertIn('978-1-60309-3', response.content.decode())


class CatalogTemplateTests(SimpleTestCase):
    """    Тест шаблона    """
    def test_homepage_template(self):
        response = self.client.get(reverse('permis:home'))
        self.assertTemplateUsed(response, 'permis/home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get(reverse('permis:home'))
        self.assertContains(response, 'E-library Application')

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('permis:home'))
        self.assertNotContains(response, 'Hello World')


class CatalogFormTests(SimpleTestCase):
    """    Тесты для форм    """
    def setUp(self):
        url = reverse('permis:home')
        self.response = self.client.get(url)

    def test_book_form(self):
        form = self.response.context.get('add_book_form')
        self.assertIsInstance(form, AddBookForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_bootstrap_class_used_for_default_styling(self):
        form = self.response.context.get('add_book_form')
        self.assertIn('class="form-control"', form.as_p())

    def test_book_form_validation_for_blank_items(self):
        add_book_form = AddBookForm(
            data={'title': '', 'ISBN': '', 'author': '', 'price': '', 'availability': ''}
        )
        self.assertFalse(add_book_form.is_valid())


class PermisURLsTest(SimpleTestCase):
    def test_main_page_url_name(self):
        response = self.client.get(reverse('permis:home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)


class CatalogModelTests(TestCase):
    """    Тест модели каталога    """
    def setUp(self):
        self.game = Catalog(
            title='Dota',
            ISBN='978-1-60309-3',
            author='Blizzard',
            price='9.99',
            availability='True'
        )

    def test_create_book(self):
        self.assertIsInstance(self.game, Catalog)

    def test_str_representation(self):
        self.assertEqual(str(self.game), "Dota")

    def test_saving_and_retrieving_book(self):
        first_game = Catalog()
        first_game.title = 'Dota'
        first_game.ISBN = '978-1-60309-3'
        first_game.author = 'Blizzard'
        first_game.price = '9.99'
        first_game.availability = 'False'
        first_game.save()

        second_game = Catalog()
        second_game.title = 'Dota 2'
        second_game.ISBN = '978-3-60124-1'
        second_game.author = 'Valve'
        second_game.price = '19.99'
        second_game.availability = 'True'
        second_game.save()

        saved_games = Catalog.objects.all()
        self.assertEqual(saved_games.count(), 2)

        first_saved_game = saved_games[0]
        second_saved_game = saved_games[1]
        self.assertEqual(first_saved_game.title, 'Dota')
        self.assertEqual(second_saved_game.author, 'Valve')

