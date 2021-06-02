from django.urls import path

from demoapp.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]