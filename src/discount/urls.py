from django.urls import path

from .views import (
    DiscountListView,
    DiscountDetailView
)

urlpatterns = [
    path('list/<str:>', DiscountListView.as_view(), name='discount-list'),
    path('detail/<str:id>', DiscountDetailView.as_view(), name='discount-detail'),
]
