from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    institute = models.CharField(max_length=255, blank=True)
    
    PLATFORM_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Twitch', 'Twitch'),
        ('TikTok', 'TikTok'),
        ('Instagram', 'Instagram'),
        ('Podcast', 'Podcast'),
    )
    main_platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='YouTube')

    def __str__(self):
        return f"{self.username} ({self.main_platform})"

class VideoIdea(models.Model):
    STATUS_CHOICES = (
        ('Idea', 'Idea'),
        ('Scripting', 'Scripting'),
        ('Recording', 'Recording'),
        ('Editing', 'Editing'),
        ('Published', 'Published'),
    )
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Idea')
    target_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ResourceLink(models.Model):
    video = models.ForeignKey(VideoIdea, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.title} for {self.video.title}"