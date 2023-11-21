from django.utils import (
    timezone,
)
from django.urls import (
    reverse,
)
from rest_framework import (
    status,
)
from clnapp.tests import (
    TestCase,
)
from django.contrib.auth.models import (
    User,
)
from clnapp.models import UserBadge, Badge
from clnapp.models.constants import (
    BADGE_PIONNEER,
    CONDITION_PIONNEER,
)


class HookPionneerTestCase(TestCase):
    def test_assign_badge_pionneer(
        self,
    ):
        """
        1. check if user has badge False
        2. user register date and check user has badge True
        """
        nb_days_pass = CONDITION_PIONNEER + 10
        user = User.objects.get(username="soro")
        badge = Badge.objects.filter(name=BADGE_PIONNEER).first()

        # 1
        user_has_badge_pionneer = UserBadge.objects.filter(
            user=user,
            badge=badge,
        ).exists()
        self.assertFalse(user_has_badge_pionneer)
        # start login user with jwt
        data = {
            "username": user.username,
            "password": "soro",
        }
        login_response = self.client.post(
            reverse("token_obtain_pair"),
            data,
            format="json",
        )
        self.assertEqual(
            login_response.status_code,
            status.HTTP_200_OK,
        )
        # - end login
        user_has_badge_pionneer = UserBadge.objects.filter(
            user=user,
            badge=badge,
        ).exists()
        self.assertFalse(user_has_badge_pionneer)

        # 2
        new_date = user.date_joined - timezone.timedelta(days=nb_days_pass)
        user.date_joined = new_date
        user.save()

        # login user with jwt
        data = {
            "username": user.username,
            "password": "soro",
        }
        login_response = self.client.post(
            reverse("token_obtain_pair"),
            data,
            format="json",
        )
        self.assertEqual(
            login_response.status_code,
            status.HTTP_200_OK,
        )

        user_has_badge_pionneer = UserBadge.objects.filter(
            user=user,
            badge=badge,
        )
        self.assertEqual(
            user_has_badge_pionneer.count(),
            1,
        )
        self.assertTrue(user_has_badge_pionneer.exists())
