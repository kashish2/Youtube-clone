from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *
from .serializers import *

from rest_framework import generics
from .utils import *
from rest_framework.pagination import CursorPagination



class YoutubeItems(generics.ListAPIView):
    search_fields = ['title', 'description']
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer


def get_videos(request):
    videos = Videos.objects.all()
    return render(request, "landing_page.html", {"videos" : videos})


def get_video_by_id(request, pk):
    video = Videos.objects.get(video_id=pk)
    return render(request, 'index.html', {"video" : video})


def fetch_new_videos(request):
    fetch_videos_from_youtube_and_store_in_db()
    return redirect(get_videos)