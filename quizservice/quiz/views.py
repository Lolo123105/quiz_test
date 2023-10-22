import requests

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ViewSet):
    @action(detail=False,
            methods=['post'])
    def get_question(self, request):
        questions_num = request.data.get('questions_num', 1)

        url = f'https://jservice.io/api/random?count={questions_num}'
        response = requests.get(url)
        response_json = response.json()

        saved_questions = []
        for question_data in response_json:
            question_id = question_data['id']
            question_text = question_data['question']
            answer_text = question_data['answer']

            while Question.objects.filter(question_id=question_id).exists():
                response = requests.get(url)
                response_json = response.json()
                question_data = response_json[0]
                question_id = question_data['id']
                question_text = question_data['question']
                answer_text = question_data['answer']

            quiz_question = Question(question_id=question_id,
                                     question_text=question_text,
                                     answer_text=answer_text)
            quiz_question.save()
            saved_questions.append(quiz_question)
        serializer = QuestionSerializer(saved_questions, many=True)
        return Response(serializer.data)
