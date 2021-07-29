from django.http import request
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
    return render(request, 'qna_detail.html', {'question': question})

def question_new(request):
    return render(request, 'new_question.html')

def question_create(request):
    new_question = Question()
    new_question.title = request.POST['title']
    new_question.writer = request.POST['writer']
    new_question.location = request.POST['location']
    new_question.content = request.POST['content']
    new_question.date = timezone.now()
    if (request.FILES.get('image') is not None) :
            new_question.image = request.FILES['image']
    new_question.save()

    return redirect('q_detail', new_question.id)

def question_edit(request, id):
    edit_question = Question.objects.get(id = id)
    return render(request, 'question_edit.html', {'question':edit_question})

def question_update(request, id):
    update_question = Question.objects.get(id = id)
    update_question.title = request.POST['title']
    update_question.writer = request.POST['writer']
    update_question.content = request.POST['content']
    update_question.date = timezone.now()
    update_question.image = request.FILES['image']
    update_question.save()

    return redirect('q_detail', update_question.id)

def question_delete(request, id):
    delete_question = Question.objects.get(id = id)
    delete_question.delete()
    return redirect('qna_list')

def answer_new(request, id):
    question = get_object_or_404(Question, pk = id)
    return render(request, 'new_answer.html', {'question':question})

def answer_create(request, id):
    question = get_object_or_404(Question, pk = id)
    new_answer = Answer(question = question, writer = request.POST['writer'], content = request.POST['content'], date = timezone.now())
    if (request.FILES.get('image') is not None) :
            new_answer.image = request.FILES['image']
    new_answer.save()

    return redirect('q_detail', id = question.id)

def answer_detail(request, id):
    answer = get_object_or_404(Answer, pk = id)
    return render(request, 'qna_answer.html', {'answer': answer})

def answer_edit(request, id):
    edit_answer = Answer.objects.get(id = id)
    return render(request, 'answer_edit.html', {'answer':edit_answer})

def answer_update(request, id):
    update_answer = Answer.objects.get(id = id)
    update_answer.writer = request.POST['writer']
    update_answer.content = request.POST['content']
    update_answer.date = timezone.now()
    update_answer.image = request.FILES['image']
    update_answer.save()

    return redirect('a_detail', update_answer.id)

def answer_delete(request, id):
    delete_answer = Answer.objects.get(id = id)
    id = delete_answer.question.id
    delete_answer.delete()
    return redirect('q_detail', id)