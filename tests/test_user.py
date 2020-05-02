import unittest
from app.models import User
class UserModelTest(unittest.TestCase):
  def setUp(self):
    '''
    test method that runs before all other tests
    '''
    self.new_user = User(password = 'victor')
  def test_password_setter(self):
    '''
    method that tests if password setter works
    '''
    self.assertTrue(self.new_user.pass_secure is not None)
  def test_no_access_password(self):
    '''
    test method that tests if passwords can be viewed by users
    '''
    with self.assertRaises(AttributeError):
      self.new_user.password

  def test_password_verification(self):
    '''
    test method that tests if password are verified corrrectly
    '''

    self.assertTrue(self.new_user.verify_password('victor'))