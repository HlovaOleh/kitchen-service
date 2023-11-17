from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PrivateDishTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Redmenol",
            password="qwerty123",
            years_of_experience=4
        )
        self.client.force_login(self.user)

    def test_cook_search(self):
        self.cook1 = get_user_model().objects.create(
            username="Satan")
        response = self.client.get(
            reverse("cook:cook-list"), {"username": "Satan"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Satan")
        self.assertNotContains(response, "aStan")
