from django.db import models
from django.conf import settings 

User = settings.AUTH_USER_MODEL 

class events(models.Model):
    name_event = models.CharField(max_length=200, blank=False)
    description_event = models.TextField(blank=True)
    image_event = models.ImageField(upload_to="events", blank=False)
    date_event = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events_created")
    participants = models.ManyToManyField(User, related_name="events_participating", blank=True) 

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.name_event} ({self.creator.first_name})"