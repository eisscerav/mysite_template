from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice, Person
from .forms import MyForm
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')#[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def table(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'ten': 10,
    }
    return render(request, 'polls/bt_table.html', context)


def search(request):
    cudaVer = request.POST['cudaVer']
    driver = request.POST['driver']
    pref = request.POST['preference']
    datetime = request.POST['datetime']
    context = {
        'cudaVer': cudaVer,
        'driver': driver
    }
    return render(request, 'polls/bt_table.html', context)


def echarts(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'polls/echarts.html', context)


def form(request):
    # GET method
    form_ = MyForm()
    context = {
        'form': form_
    }
    return render(request, 'polls/my_form.html', context)
