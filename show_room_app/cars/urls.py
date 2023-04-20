from django.urls import path
from cars.views import CarListView, CarDetailListView, CarCreateView


urlpatterns = [
    path("", CarListView.as_view()),
    path("<int:pk>/", CarDetailListView.as_view()),
    path("create/", CarCreateView.as_view()),
]
