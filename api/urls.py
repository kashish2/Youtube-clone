from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_videos, name="get_videos"),
    path('/<str:pk>', views.get_video_by_id, name="get_details_of_a_video"),
    path('check', views.fetch_new_videos, name="fetch_new_videos"),
]
