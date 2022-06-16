import re
from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse
# reverse is also called generateUrlFromViewName, it is used especially for redirecting page.

class QuestionModelTests (TestCase):
    def test_was_published_recently_with_future_question(self):
        # was_published_recently() should return False for questions whose pub_date is in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        # was_published_recently() should return False for questions whose pub_date is older than 1 day.
        time = timezone.now() - datetime.timedelta(days =1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        # was_published_recently() should return True for questions whose pub_date is within the last day.
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)



# testing IndexView 
# first create a shortcut function 
def create_question(question_text, days):
    # create a question with given 'question_text' and published the given number of days offset to now
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        # if no question exist, an appropriate msg is displayed
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_questions(self):
        question = create_question(question_text="Past question", days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
    
    def test_future_questions(self):
        # future questions aren't displayed on the index page
        question = create_question(question_text="Future question", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_future_and_past_questions(self):
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_two_past_questions(self):
        # the question index page may display multiple questions.
        question1 = create_question(question_text="Past Question 1", days = -30)
        question2 = create_question(question_text="Past Question 2", days = -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question2,question1])