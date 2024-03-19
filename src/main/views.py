from rest_framework.generics import ListAPIView

from .models import Stories
from .serializers import StoriesSerializers


class StoriesView(ListAPIView):
    queryset = Stories.objects.order_by("-id")
    serializer_class = StoriesSerializers
