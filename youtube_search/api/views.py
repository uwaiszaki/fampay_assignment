from rest_framework import generics, pagination, filters
from rest_framework.pagination import PageNumberPagination

from youtube_search.models import Keyword, Video
from .serializers import VideoSerializer


class SearchVideo(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'keyword__name']
    ordering_fields = ['published_at']

