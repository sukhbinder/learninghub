from django.urls import path
from spelling.views import home_view, WordUpdateView, WordDeleteView, ListWordsView

urlpatterns = [
    path('', home_view, name="home"),
    path('api/<int:pk>/', WordUpdateView.as_view(), name='update-word'),
    path('api/<int:pk>/delete/', WordDeleteView.as_view(), name='delete-word'),
    path('api/', ListWordsView.as_view(), name='list-word'),
]
