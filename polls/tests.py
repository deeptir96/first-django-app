from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question

# Create your tests here.
class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_oldquestion(self):
		time = timezone.now() - datetime.timedelta(days=30)
		old_question=Question(pub_date=time)
		self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recentquestion(self):
		time=timezone.now()-datetime.timedelta(hours=1)
		recent_question=Question(pub_date=time)
		self.assertEqual(recent_question.was_published_recently(), True)
		