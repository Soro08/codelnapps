from django.test import TestCase as DjangoTestCase


class TestCase(DjangoTestCase):
    fixtures = ["users.json", "model3d.json", "badges.json", "userbadges.json"]

    def setUp(self):
        pass
