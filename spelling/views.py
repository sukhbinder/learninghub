from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponseRedirect

from spelling.serializers import WordSerializer
from spelling.models import Word, Subject
from .forms import UploadFileForm
# Create your views here.


def handle_uploaded_file(file):
    sub_dict = {sub.name: sub for sub in Subject.objects.all()}
    first_line = None
    for line in file:
        line = str(line.decode("ascii")).strip()
        if first_line is None:
            first_line = line
            assert first_line in sub_dict.keys(),  "{} Subject not listed in {}".format(
                first_line, sub_dict.keys())
            continue
        try:
            question, answer = line.strip().split(",")
            w = Word(question=str(question), answer=str(
                answer), subject=sub_dict[first_line])
            w.save()
        except Exception as ex:
            print(ex)
            pass


def home_view(request,pk):
    return render(request, 'spelling/home.html', {"data": "Hello World"})

def index_view(request):
    return render(request, 'spelling/index.html', {"data": "Hello World"})


def subject_view(request):
    a = list(set([(obj.subject.id, str(obj.subject.name))
                  for obj in Word.objects.all()]))
    return JsonResponse(a, safe=False)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('spelling/')
    else:
        form = UploadFileForm()
    return render(request, 'spelling/upload.html', {'form': form})


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
