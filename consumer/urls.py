# urls.py
from django.urls import path
from .views import (
    ConsumerView,
    ManageConsumerView
)

urlpatterns = [
    path('', ConsumerView.as_view(), name='consumer_list'),
    path('manage_consumer/', ManageConsumerView.as_view(), name='manage_consumer'),
]
