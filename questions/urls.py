from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:product_id>/add_question/',
        views.add_question,
        name='add_question'),
    path(
        '<int:question_id>/add_reply/',
        views.add_reply,
        name='add_reply'),
]
