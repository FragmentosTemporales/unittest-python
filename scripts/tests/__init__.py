from flask_testing import TestCase
from app import create_app


class BaseTestCase(TestCase):
    """ Base Tests """
    def create_app(self):
        app = create_app(test_mode=True)
        return app
