from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,render
from django.urls import reverse
from .models import Question,Choice
# Create your views here.

# Qustion에서 객체들을 뽑아 view에 전달
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)

# 전달받은 question_id로 알맞은 객체 뽑아 뷰로 전달
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def vote(request, question_id):
    # 전달받은 question_id로 객체 찾기
    question = get_object_or_404(Question,pk=question_id)
    try:
        # 그 question_id의 choice들 중에 사용자가 선택한 chocie를 post로 넘어온 값으로 찾기
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question' : question,
            'error_message' : "You didn't select a choice"
        })
    else:
        # 투표수 ++하고 저장, results로 이동
        selected_choice.votes += 1
        selected_choice.save()
        # post로 데이터를 성공적으로 처리한 경우 대부분 HttpResponseRedirect 이용을 권장함
        return HttpResponseRedirect(reverse('results',args=(question.id,)))

# question에 대한 정보를 보여줌
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
