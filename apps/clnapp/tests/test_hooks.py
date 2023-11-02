from clnapp.tests import TestCase
from clnapp.models import Model3d


class Model3dHookTestCase(TestCase):
    def test_add_less_than_5_model3d(self):
        """
        Adds 4 model3d object and check user has not collector badge
        """
        pass

    def test_add_greater_than_5_model3d(self):
        """
        Adds 5 model3d object and check user has collector badge
        """
        pass
