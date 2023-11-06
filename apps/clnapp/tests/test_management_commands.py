from io import StringIO
from django.core.management import (
    call_command,
)
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
from clnapp.models import (
    UserBadge,
    Badge,
    Model3d,
)
from clnapp.models.constants import (
    BADGE_PIONNEER,
    BADGE_START,
    CONDITION_PIONNEER,
    CONDITION_START,
)


class ManagementCommandsTestCase(TestCase):
    def test_assign_badge_pionneer(
        self,
    ):
        """
        1. run commands check if user has badge False
        2. user register date and check user has badge True
        """
        out = StringIO()
        nb_days_pass = CONDITION_PIONNEER + 10
        user = User.objects.get(id=1)
        badge = Badge.objects.filter(name=BADGE_PIONNEER).first()

        # 1
        user_has_badge_pionneer = UserBadge.objects.filter(
            user=user,
            badge=badge,
        ).exists()
        self.assertFalse(user_has_badge_pionneer)
        call_command(
            "assign_badge_pionneer",
            stdout=out,
        )
        user_has_badge_pionneer = UserBadge.objects.filter(
            user=user,
            badge=badge,
        ).exists()
        self.assertFalse(user_has_badge_pionneer)

        # 2
        new_date = user.date_joined - timezone.timedelta(days=nb_days_pass)
        user.date_joined = new_date
        user.save()
        call_command(
            "assign_badge_pionneer",
            stdout=out,
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

    def test_assign_badge_start(
        self,
    ):
        """
        1. run commands check if user has badge False
        2. update number_of views and check user has badge True
        """
        out = StringIO()
        model3d = Model3d.objects.last()
        badge = Badge.objects.filter(name=BADGE_START).first()

        # 1
        self.assertFalse(model3d.nb_views > CONDITION_START)
        call_command(
            "assign_badge_start",
            stdout=out,
        )
        user_has_badge_star = UserBadge.objects.filter(
            user=model3d.author,
            badge=badge,
        ).exists()

        self.assertFalse(user_has_badge_star)
        for _ in range((CONDITION_START - model3d.nb_views) + 5):
            urls = reverse(
                "model3d-detail",
                kwargs={"pk": model3d.id},
            )
            response = self.client.get(
                urls,
                format="json",
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK,
            )

        # 2
        model3d = Model3d.objects.get(id=model3d.id)

        call_command(
            "assign_badge_start",
            stdout=out,
        )

        user_has_badge_star = UserBadge.objects.filter(
            user=model3d.author,
            badge=badge,
        )
        self.assertTrue(model3d.nb_views > CONDITION_START)
        self.assertEqual(
            user_has_badge_star.count(),
            1,
        )
        self.assertTrue(user_has_badge_star.exists())
