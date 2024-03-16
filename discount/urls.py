from django.urls import path

from .views import (
    DiscountListView
)

urlpatterns = [
    path('list', DiscountListView.as_view(), name='discount-list'),
]
