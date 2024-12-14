from django.shortcuts import render, redirect
from .models import Question, QuizSession, UserAnswer
import random

def home(request):
    return render(request, 'home.html')

def start_quiz(request):
    session = QuizSession.objects.create()
    # Select 5 random questions from the database
    questions = list(Question.objects.all())
    selected_questions = random.sample(questions, k=min(5, len(questions)))  # Get 5 or fewer if not enough questions
    request.session['quiz_questions'] = [q.id for q in selected_questions]  # Store question IDs in session
    request.session['current_question_index'] = 0  # Initialize question index
    return redirect('get_question', session_id=session.id)

def get_question(request, session_id):
    question_ids = request.session.get('quiz_questions', [])
    current_index = request.session.get('current_question_index', 0)

    if current_index >= len(question_ids):
        return redirect('results', session_id=session_id)  # Redirect to results if all questions answered

    question_id = question_ids[current_index]
    question = Question.objects.get(id=question_id)

    return render(request, 'quiz.html', {'question': question, 'session_id': session_id})

def submit_answer(request, session_id):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_answer = request.POST.get('answer')
        question = Question.objects.get(id=question_id)

        is_correct = selected_answer == question.correct_answer
        session = QuizSession.objects.get(id=session_id)
        UserAnswer.objects.create(
            quiz_session=session,
            question=question,
            selected_answer=selected_answer,
            is_correct=is_correct
        )

        # Update the current question index in the session
        request.session['current_question_index'] += 1

        return redirect('get_question', session_id=session_id)

def results(request, session_id):
    session = QuizSession.objects.get(id=session_id)
    user_answers = UserAnswer.objects.filter(quiz_session=session)

    total_questions = user_answers.count()
    correct_answers = user_answers.filter(is_correct=True).count()
    incorrect_answers = total_questions - correct_answers

    return render(request, 'results.html', {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
        'user_answers': user_answers
    })