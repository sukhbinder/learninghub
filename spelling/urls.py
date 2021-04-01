from django.urls import path
from spelling import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('api/<int:pk>/', views.WordUpdateView.as_view(), name='update-word'),
    path('api/<int:pk>/delete/', views.WordDeleteView.as_view(), name='delete-word'),
    path('api/', views.ListWordsView.as_view(), name='list-word'),
    path('subject/<int:subject>', views.ListWordsViewbySubject.as_view(), name='list-word-subject'),
    path('subjects', views.subject_view, name="subjects"),
    path('upload', views.upload_file, name="upload"),
    path('<int:pk>', views.home_view, name="home"),
    path('test/<int:pk>', views.test_view, name="test-view"),
    
]
