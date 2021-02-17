from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader 
from django.shortcuts import get_object_or_404, render
from django.urls import reverse 
from django.views import generic

from .models import Choice, Question


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def index(request):
#     # 1
#     # return HttpResponse("Hello, world. You're at the polls index.")
    
#     # 2
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)

#     # 3 
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))

#     # 4 
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     # 1
#     # return HttpResponse("You're looking at question %s." % question_id)

#     # 2 404예외처리시.
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question':question})

#     # 3 404예외처리다른방법. you can express like that with out try..except   by from django.shortcuts import get_object_or_404
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     # return HttpResponse("You're voting on question %s."% question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         # request.POST는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체.
#         # request.POST['choice']는 선택된 설문의 ID를 문자열로 반환.
#         # request.POST의 값은 항상 문자열.
#         # Django는 같은 방법으로 GET 자료에 접근하기 위해 request.GET를 제공.
#         # 하지만 POST 요청을 통해서만 자료가 수정되게하기위해서, 명시적으로 코드에 request.POST 를 사용
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after Successfully dealing
#         # with Post data, This prevents data from being posted twice if a user hits the Back Button
#         # Aessfully dealing with POST data.
#         # This tip isn’s the Python comment above points out, you should always return an HttpResponseRedirect after succt specific to Django;
#         # It’s good Web development practice in general.

#         # POST로 request 했을 경우, HttpResponseRedirect해준다. POST로 뷰를 호출한 경우 REDIRECT한다고 세트라고생각하면된다.
#         # reverse() url하드코딩하지않기 위해서 사용.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))