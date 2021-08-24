import sys
sys.path.append(r"/home/fanxin/github/mysite_template")
import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite_template.settings")
django.setup()


from polls.models import Question, Choice
from django.utils import timezone
import datetime
import random


def genData():
    print("Generate foo data into database...")
    questions = [chr(x) for x in range(65, 91)]
    choices = [chr(x) for x in range(97, 123)]
    numberOfQuestion = random.randint(2, 5)
    for each in range(numberOfQuestion):
        questionList = random.sample(questions, 5)
        questionText = ''.join(questionList)
        q = Question(question_text=questionText, pub_date=timezone.now())
        q.save()
        for i in range(3):
            choiceList = random.sample(choices, 3)
            choiceText = ''.join(choiceList)
            rand = random.randint(1, 10)
            q.choice_set.create(choice_text=choiceText, votes=rand)
    # for each in range(count):
    #     char = random.randint(65, 91)
    #     question.append(char)
    #     qtext = ''.join(question)
    #     q = Question(question_text=qtext, pub_date=timezone.now())
    #     q.save()
    #     for choice in range(3):
    #         pass
    # q = Question(question_text=qtext, pub_date=timezone.now())
    # q.save()
    # q.choice_set.create(choice_text="abc", votes=3)
    # q.choice_set.create(choice_text="def", votes=2)
    # q.choice_set.create(choice_text="ghi", votes=5)


if __name__ == "__main__":
    genData()


