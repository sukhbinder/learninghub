from django.urls import path
from spelling.views import home_view, index_view, WordUpdateView, WordDeleteView, ListWordsView,ListWordsViewbySubject, subject_view, upload_file


urlpatterns = [
    path('', index_view, name="index"),
    path('api/<int:pk>/', WordUpdateView.as_view(), name='update-word'),
    path('api/<int:pk>/delete/', WordDeleteView.as_view(), name='delete-word'),
    path('api/', ListWordsView.as_view(), name='list-word'),
    path('subject/<int:subject>', ListWordsViewbySubject.as_view(), name='list-word-subject'),
    path('subjects', subject_view, name="subjects"),
    path('upload', upload_file, name="upload"),
    path('<int:pk>', home_view, name="home"),
    
]
