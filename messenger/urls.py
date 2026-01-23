from django.urls import path
from . import views

urlpatterns = [
    path("messages/", views.inbox, name="inbox"),
    path("messages/send/", views.send_message, name="send_message"),
    path("messages/<int:pk>/", views.message_detail, name="message_detail"),
]