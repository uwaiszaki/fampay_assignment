from rest_framework import serializers

from youtube_search.models import Keyword, Video


class KeywordBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    keyword = KeywordBaseSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Keyword
        fields = ['name', 'is_active', 'videos']

