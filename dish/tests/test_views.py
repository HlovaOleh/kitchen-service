from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from dish.models import DishType, Dish

DISHTYPE_URL = reverse("dish:dish_type-list")
DISH_URL = reverse("dish:dish-list")
COOKS_URL = reverse("cook:cook-list")


class PublicDishTypeTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(DISHTYPE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user",
            password="qwerty1234",
            years_of_experience=4
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Test")
        DishType.objects.create(name="Qwer")
        res = self.client.get(DISHTYPE_URL)
        self.assertEqual(res.status_code, 200)
        dishtype = DishType.objects.all()
        self.assertEqual(
            list(res.context["dishtype_list"]),
            list(dishtype),
        )
        self.assertTemplateUsed(res, "dish/dishtype_list.html")

    def test_search_dish_type_by_name(self):
        DishType.objects.create(name="Test")
        searched_name = "Test"
        response = self.client.get(
            DISHTYPE_URL,
            {"name": searched_name}
        )
        self.assertEqual(response.status_code, 200)
        dish_type_in_context = DishType.objects.filter(
            name__icontains=searched_name
        )
        self.assertQuerysetEqual(
            response.context["dishtype_list"], dish_type_in_context
        )


class PublicDishTest(TestCase):

    def test_dish_login_required(self):
        res = self.client.get(DishType)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Redmenol",
            password="qwerty123",
            years_of_experience=4
        )
        self.client.force_login(self.user)

    def test_retrieve_dish(self):
        dishtype = DishType.objects.create(name="test_dish_type")
        Dish.objects.create(
            name="test_name",
            price=20,
            dish_type=dishtype
        )

        response = self.client.get(DISH_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "dish/dish_list.html")
