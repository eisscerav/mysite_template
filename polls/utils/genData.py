import sys, os, json
import argparse
#todo: make path configurable or don't set to a const path
sys.path.append(r"/home/fanxin/github/mysite_template")
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite_template.settings")
django.setup()


from polls.models import Question, Choice, Person
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


def genJson():
    print("Generate foo data in json fashion")
    mydict = {}
    mydict["id"] = 1
    mydict["name"] = "football"
    mydict["price"] = 100
    json_obj = json.dumps(mydict)
    print(json_obj)
    with open("myData.json", "w") as output:
        json.dump(mydict, output)


def genPerson():
    print("Generate foo data for table Person")
    foo_names = [chr(x) for x in range(65, 91)]
    numOfPerson = random.randint(1, 10)
    for each in range(numOfPerson):
        name = random.sample(foo_names, random.randint(3,7))
        name = ''.join(name)
        person = Person(name=name, age=random.randint(18, 22), score=random.randint(60, 100))
        person.save()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--person', action='store_true')
    parser.add_argument('--data', action='store_true')
    args = parser.parse_args()
    if args.json:
        genJson()
    if args.person:
        genPerson()
    if args.data:
        genData()


if __name__ == "__main__":
    main()
