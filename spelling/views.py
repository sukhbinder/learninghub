from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponseRedirect

from spelling.serializers import WordSerializer
from spelling.models import Word, Subject
from .forms import UploadFileForm
import numpy as np
# Create your views here.

def get_sub_voice_chapter(line):
    linelist = line.strip().split(',')
    subject = linelist[0]
    voiceonly = False
    chapter = 0
    if len(linelist) >1:
        if isinstance(linelist[1], str):
            if "true" in linelist[1].lower():
                 voiceonly = True
        elif isinstance(linelist[2], int):
            chapter = int(linelist[2])
    if len(linelist) > 2:
        if isinstance(linelist[2], int):
            chapter = int(linelist[2])
    return subject, voiceonly, chapter

def handle_uploaded_file(file):
    sub_dict = {sub.name: sub for sub in Subject.objects.all()}
    first_line = None
    for line in file:
        line = str(line.decode("ascii")).strip()
        if first_line is None:
            first_line, voiceonly, chapter = get_sub_voice_chapter(line)
            assert first_line in sub_dict.keys(),  "{} Subject not listed in {}".format(
                first_line, sub_dict.keys())
            continue
        try:
            question, answer = line.strip().split(",")
            w = Word(question=str(question), answer=str(
                answer), subject=sub_dict[first_line],
                chapter=chapter, isvoiceonly=voiceonly
                )
            w.save()
        except Exception as ex:
            print(ex)
            pass


def home_view(request,pk):
    return render(request, 'spelling/home.html', {"data": "Hello World"})

def index_view(request):
    data = list(set([(obj.id, str(obj.name))
                  for obj in Subject.objects.all()]))

    return render(request, 'spelling/index.html', {"data": data})


def subject_view(request):
    a = list(set([(obj.id, str(obj.name))
                  for obj in Subject.objects.all()]))
    return JsonResponse(a, safe=False)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/spelling/')
    else:
        form = UploadFileForm()
    return render(request, 'spelling/upload.html', {'form': form})


def test_view(request, pk):
    # data = np.array([(obj.question, obj.answer) for obj in Word.objects.all() if obj.subject.id == sub_id])
    # np.random.shuffle(data)
    # data = data[:num].tolist()
    return render(request, 'spelling/test.html', {"data": "Hello World"})

class WordUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDeleteView(generics.DestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class ListWordsView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class ListWordsViewbySubject(generics.ListCreateAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        """
        This view should return a list of all words by
        the subject passed in the URL
        """
        subject = self.kwargs['subject']
        if subject is not None:
            return Word.objects.filter(subject=subject)
        else:
            return Word.objects.all()


