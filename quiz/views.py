# views.py

from django.shortcuts import render, redirect
from .models import Quiz, Question, Answer, UserResponse
from django.contrib.auth.decorators import login_required

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})

@login_required
def submit_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                user_response = UserResponse(user=request.user, question=question, selected_answer=selected_answer)
                user_response.save()

        return redirect('quiz_result', quiz_id=quiz_id)

    return render(request, 'submit_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def quiz_result(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    user_responses = UserResponse.objects.filter(user=request.user, question__in=questions)

    total_questions = len(questions)
    total_correct = sum(response.selected_answer.is_correct for response in user_responses)

    return render(request, 'quiz_result.html', {
        'quiz': quiz,
        'total_questions': total_questions,
        'total_correct': total_correct,
    })
