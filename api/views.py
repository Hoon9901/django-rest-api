from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
