from django.urls import path

from .views import (
    StoriesView,
    AsmanDetailView
)

urlpatterns = [
    path('stories', StoriesView.as_view(), name='stories'),
    path('asman-detail/', AsmanDetailView.as_view(), name='asman-detail')
]
