import logging
from .models import *
from datetime import datetime, timedelta   

# Google API
from apiclient.discovery import build
from youtube_fetch_api import settings
 
logger = logging.getLogger("application")


def fetch_videos():
    last_request_time = datetime.now() - timedelta(weeks=62)


    try:
        youtube = build('youtube', 'v3', developerKey=settings.GOOGLE_API_KEYS[0])
        request = youtube.search().list(
            q="trending", 
            part="snippet", 
            order="date", 
            maxResults=20,
            publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z')
        )
        result = request.execute()
    except Exception as e:
        logger.info("got error while fetching videos")
    return result 

def get_video_by_id(video_id):

    try:
        youtube = build('youtube', 'v3', developerKey='AIzaSyBXJTKThST3TEgcHZLxO1qoMejvw-X6CZk')
        request = youtube.videos().list(
            part = "statistics", id = video_id, maxResults = 1
        )
        result = request.execute()
    except Exception as e:
        logger.info("got error while fetch a video details")
    return result['items'][0]

def get_channel(channel_id):
    try:
        youtube = build('youtube', 'v3', developerKey='AIzaSyBXJTKThST3TEgcHZLxO1qoMejvw-X6CZk')
        request = youtube.channels().list(
            part = "snippet, statistics", id = channel_id
        )
        result = request.execute()
    except Exception as e:
        logger.info("got error while fetching channel details")
    return result['items'][0]


def fetch_videos_from_youtube_and_store_in_db():
    response = fetch_videos()

    for item in response['items']:
        
        video_id = item['id'].get('videoId', "")
        video_title = item['snippet'].get('title', "")
        description = item['snippet'].get('description', "")
        video_thumbnail = item['snippet']['thumbnails']['default'].get('url', "")
        channel_id = item['snippet'].get('channelId', "")
        channel_title = item['snippet'].get('channelTitle', "")

        if video_id is "" or channel_id is "":
            continue

        req2 = get_video_by_id(video_id)
        req3 = get_channel(channel_id)

        video_view_count = req2['statistics'].get('viewCount', 0)
        video_like_count = req2['statistics'].get('likeCount', 0)
        video_dislike_count = req2['statistics'].get('dislikeCount', 0)
        channel_thumbnail = req3['snippet']['thumbnails']['default'].get('url', "")
        channel_subs = req3['statistics'].get('subscriberCount', 0)
        channel_description = req3['snippet'].get('description', "")

        channel_subs = int(channel_subs)

        if len(Videos.objects.filter(video_title=video_title)) != 0:
            Videos.objects.filter(video_title=video_title).update(
                video_id=video_id,
                video_title=video_title,
                video_thumbnail=video_thumbnail,
                video_view_count=video_view_count,
                video_like_count=video_like_count,
                video_dislike_count=video_dislike_count,
                description=description,
                channel_title=channel_title,
                channel_description=channel_description,
                channel_subs=channel_subs,
                channel_thumbnail=channel_thumbnail
            )
        
        else:
            Videos.objects.create(
                video_id=video_id,
                video_title=video_title,
                video_thumbnail=video_thumbnail,
                video_view_count=video_view_count,
                video_like_count=video_like_count,
                video_dislike_count=video_dislike_count,
                description=description,
                channel_title=channel_title,
                channel_description=channel_description,
                channel_subs=channel_subs,
                channel_thumbnail=channel_thumbnail
            )
    
    logger.info("Objects created succefully")
