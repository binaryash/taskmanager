from django.db import models
import uuid

class ScrapingJob(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    # Contains the json output data
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.job_id)
