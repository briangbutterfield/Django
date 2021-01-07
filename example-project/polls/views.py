#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last five published questions.
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))



""" Before Generic Views...

def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    # output = ', '.join([q.question_text for q in latest_question_list])

    # Loads template.
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')    
    #context = {'latest_question_list': latest_question_list,}
    #return HttpResponse(template.render(context, request))

    # Uses render https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-render
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    # Ref:  https://docs.djangoproject.com/en/3.1/intro/tutorial03/#raising-a-404-error
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist.")
    #return render(request = request, template_name = 'polls/details.html', context = {'question': question})

    # Ref:  https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-get-object-or-404
    question = get_object_or_404(Question, pk = question_id)
    return render(request = request, template_name = 'polls/detail.html', context = {'question': question})


def results(request, question_id):
    #response = "You're looking at the the results of question %s."
    #return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})

"""