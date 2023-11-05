from io import StringIO
from django.core.management import call_command
from clnapp.tests import TestCase


class ManagementCommandsTestCase(TestCase):
    def test_assign_badge_pionneer(self):
        """
        1. run commands check if user has badge False
        2. adds models and check user has badge True
        """
        out = StringIO()
        call_command("assign_badge_pionneer", stdout=out)
        self.assertIn("badge distribués", out.getvalue())

    def test_assign_badge_start(self):
        """
        1. run commands check if user has badge False
        2. update number_of views and check user has badge True
        """
        pass
