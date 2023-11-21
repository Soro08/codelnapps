from django.urls import (
    reverse,
)
from rest_framework import (
    status,
)
from clnapp.tests import (
    TestCase,
)

from clnapp.models import (
    UserBadge,
    Badge,
    Model3d,
)
from clnapp.models.constants import (
    BADGE_STAR,
    CONDITION_STAR,
)


class HookStarTestCase(TestCase):
    def test_assign_badge_star(
        self,
    ):
        """
        1. check if user has badge False
        2. update number_of views and check user has badge True
        """
        model3d = Model3d.objects.last()
        badge = Badge.objects.filter(name=BADGE_STAR).first()

        # 1
        self.assertFalse(model3d.nb_views > CONDITION_STAR)

        user_has_badge_star = UserBadge.objects.filter(
            user=model3d.author,
            badge=badge,
        ).exists()

        self.assertFalse(user_has_badge_star)
        for _ in range((CONDITION_STAR - model3d.nb_views) + 5):
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

        user_has_badge_star = UserBadge.objects.filter(
            user=model3d.author,
            badge=badge,
        )
        self.assertTrue(model3d.nb_views > CONDITION_STAR)
        self.assertEqual(
            user_has_badge_star.count(),
            1,
        )
        self.assertTrue(user_has_badge_star.exists())
