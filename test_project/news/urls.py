from django.urls import path

from .views import NewView


app_name = "news"

urlpatterns = [
    path('news/', NewView.as_view()),
    path('news/<int:pk>', NewView.as_view())
]