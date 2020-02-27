from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from wiki.models import Page
from api.serializers import PageSerializer

class PageList(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageView(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer