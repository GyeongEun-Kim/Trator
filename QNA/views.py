from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.utils import timezone
from django.contrib.auth.models import User
from Account.models import CustomUser
from django.core.paginator import Paginator

# Create your views here.

def question_list(request):
    question_list = Question.objects.all().order_by('-id')
    paginator = Paginator(question_list, 5)
    page = request.GET.get('page')
    question_list = paginator.get_page(page)
    context = {'question_list': question_list}
    return render(request, 'qna_list.html', context)

def question_detail(request, id):
    question = get_object_or_404(Question, pk = id)
    return render(request, 'qna_detail.html', {'question': question})

def question_new(request):
    return render(request, 'new_question.html')

def question_create(request):
    new_question = Question()
    new_question.author = request.user
    new_question.title = request.POST['title']
    new_question.writer = request.user.username
    new_question.location = request.POST['location']
    new_question.content = request.POST['content']
    new_question.date = timezone.localtime()
    new_question.vote = False
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
    update_question.content = request.POST['content']
    update_question.date = timezone.localtime()
    if (request.FILES.get('image') is not None) :
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
    new_answer = Answer(question = question, author = request.user ,writer = request.user.username, content = request.POST['content'], date = timezone.localtime())
    if (request.FILES.get('image') is not None) :
            new_answer.image = request.FILES['image']
    new_answer.save()

    return redirect('q_detail', id = question.id)

def answer_edit(request, id):
    edit_answer = Answer.objects.get(id = id)
    return render(request, 'answer_edit.html', {'answer':edit_answer})

def answer_update(request, id):
    update_answer = Answer.objects.get(id = id)
    update_answer.content = request.POST['content']
    update_answer.date = timezone.localtime()
    if (request.FILES.get('image') is not None) :
        update_answer.image = request.FILES['image']
    update_answer.save()

    return redirect('q_detail', update_answer.question.id)

def answer_delete(request, id):
    delete_answer = Answer.objects.get(id = id)
    id = delete_answer.question.id
    delete_answer.delete()
    return redirect('q_detail', id)

def question_search(request):
    search_location = request.GET['location']
    search_list = Question.objects.filter(location = search_location)
    return render(request, 'qna_list.html', {'question_list':search_list})

def answer_adopt(request, id):
    adopted_answer = Answer.objects.get(id = id)
    adopting_question = Question.objects.get(id = adopted_answer.question.id)
    # user = CustomUser.objects.get(pk = adopted_answer.author.pk)
    # user.point = user.point + 1000
    adopted_answer.like = True
    adopted_answer.author.point += 1000
    adopting_question.vote = True
    # user.save()
    adopting_question.save()
    adopted_answer.save()
    adopted_answer.author.save()
    return redirect('q_detail', adopting_question.id)

def answer_another(request, id):
    question = get_object_or_404(Question, pk = id)
    return render(request, 'qna_another_answer.html', {'question': question})
