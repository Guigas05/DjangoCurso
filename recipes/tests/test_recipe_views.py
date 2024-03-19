from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={ 'category_id' : 1}))
        self.assertIs(view.func, views.category)

    def test_recipes_detail_view_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs= { 'id' : 1}))
        self.assertIs(view.func, views.recipe)