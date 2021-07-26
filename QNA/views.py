from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.utils import timezone

# Create your views here.

def question_list(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'qna_list.html', context)

def question_detail(request, id):
    question = get_object_or_404(Question, pk = id)
    context = {'question': question}
    return render(request, 'qna_detail.html', context)

def question_new(request):
    return render(request, 'new_question.html')

def question_create(request):
    new_question = Question()
    new_question.title = request.POST['title']
    new_question.writer = request.POST['writer']
    new_question.location = request.POST['location']
    new_question.content = request.POST['content']
    new_question.date = timezone.now()
    new_question.save()

    return redirect('detail', new_question.id)
