from django.shortcuts import render
from rest_framework import generics

from spelling.serializers import WordSerializer
from spelling.models import Word

# Create your views here.


def home_view(request):
    return render(request, 'spelling/home.html', {"data": "Hello World"})


class WordUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDeleteView(generics.DestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class ListWordsView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
