from django.shortcuts import render
from .models import Question

def index_view(request):
    return render(request=request, template_name='index.html')

def quiz(request):
    if request.method == 'POST':
        correct = 0
        total = 4
        questions = Question.objects.all()
        for q in questions:
            total += 1
            if q.ans == request.POST.get('question_'+str(total)):
                correct += 1
        percent = round((correct*100)/17,1)
        context = {
            'total':total,
            'correct':correct,
            'percent':percent
        }
        return render(request,'quiz_result.html',context)
    else:
        questions = Question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz.html',context)
    
def valentinee(request):
    return render(request=request, template_name='valentine.html')

def end(request):
    return render(request=request, template_name='end.html')

def no_end(request):    
    return render(request=request, template_name='no_end.html')