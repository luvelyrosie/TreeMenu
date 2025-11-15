from django.test import TestCase, RequestFactory
from django.template import Template, Context
from .models import MenuItem


class MenuTagTests(TestCase):
    def setUp(self):
        self.rf = RequestFactory()

        MenuItem.objects.create(menu='main_menu', title='Home', url='/', order=1)

        parent = MenuItem.objects.create(menu='main_menu', title='Burgers', url='/burgers/', order=2)
        MenuItem.objects.create(menu='main_menu', title='Chicken Burger', parent=parent, url='/burgers/chicken/', order=1)

        MenuItem.objects.create(menu='main_menu', title='About', named_url='about', order=3)


    def test_draw_menu_renders_and_expands_active(self):
        template = Template("{% load draw_menu %}{% draw_menu 'main_menu' %}")
        request = self.rf.get('/burgers/')
        context = Context({'request': request})

        with self.assertNumQueries(1):
            rendered = template.render(context)

        self.assertIn('Burgers', rendered)
        self.assertIn('Chicken Burger', rendered)


    def test_named_url_resolves(self):
        template = Template("{% load draw_menu %}{% draw_menu 'main_menu' %}")
        request = self.rf.get('/about/')
        context = Context({'request': request})

        rendered = template.render(context)
        self.assertIn('About', rendered)