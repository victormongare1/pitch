from app.models import Comment,User,Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_victor = User(username = 'victor',password = 'victor', email = 'victor@ms.com')
        self.new_pitch = Pitch(id=1,title='Test',description='This is a test pitch',category="interview",user = self.user_victor,upvotes=0,downvotes=0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title,'Test')
        self.assertEquals(self.new_pitch.description,'This is a test pitch')
        self.assertEquals(self.new_pitch.category,"interview")
        self.assertEquals(self.new_pitch.user,self.user_victor)

    def test_save_pitch(self):
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)