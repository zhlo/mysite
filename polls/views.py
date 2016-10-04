from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello, world!!')

def hello(request):
	return HttpResponse('return a hello function')

def detail(request, question_id):
    # latest_question_list = Question.objects.get(pk=question_id)
    # output = ', '.join([q.question_text for q in latest_question_list])
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
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
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
