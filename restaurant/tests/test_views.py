from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import DishType, Dish

DISHTYPE_URL = reverse("restaurant:dish_type-list")
DISH_URL = reverse("restaurant:dish-list")
COOKS_URL = reverse("restaurant:cook-list")


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
        self.assertTemplateUsed(res, "restaurant/dishtype_list.html")

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
        self.assertTemplateUsed(response, "restaurant/dish_list.html")

    def test_cook_search(self):
        self.cook1 = get_user_model().objects.create(
            username="Satan")
        response = self.client.get(
            reverse("restaurant:cook-list"), {"username": "Satan"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Satan")
        self.assertNotContains(response, "aStan")
