from django.shortcuts import render
from rest_framework import generics, filters
from .models import Question
from .serializers import QuestionSerializer


# Create your views here.
class QuestionAPIView(generics.ListCreateAPIView):
    search_fields = ['question_text', 'author']
    filter_backends = (filters.SearchFilter, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



