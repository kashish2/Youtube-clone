from django.db import models

class Videos(models.Model):
    video_id = models.TextField(null=True,blank=True)
    video_title = models.TextField(null=True,blank=True)
    video_thumbnail = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    video_view_count = models.IntegerField(null=True,blank=True)
    video_like_count = models.IntegerField(null=True,blank=True)
    video_dislike_count = models.IntegerField(null=True,blank=True)
    channel_title = models.TextField(null=True,blank=True)
    channel_thumbnail = models.TextField(null=True,blank=True)
    channel_description = models.TextField(null=True,blank=True)
    channel_subs = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.video_title
