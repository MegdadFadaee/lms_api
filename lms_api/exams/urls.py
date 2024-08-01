from django.urls import path

from . import views

urlpatterns = [
    # ex: /exams/
    path("", views.index, name="index"),
    # ex: /exams/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /exams/5/choices/
    path("<int:question_id>/choices/", views.choices, name="choices"),
]
