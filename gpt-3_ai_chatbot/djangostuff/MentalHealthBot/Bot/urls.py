from django.urls import path

from Bot.views import chatbot_view


urlpatterns = [
    path('', chatbot_view),
    path('chatbot/', chatbot_view, name='chatbot'),
]