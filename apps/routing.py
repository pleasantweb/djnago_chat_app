from apps.consumers import MySyncConsumer
from django.urls import path

ws_urlpatterns=[
    path('ws/sc/<str:group_name>/',MySyncConsumer.as_asgi()),
]