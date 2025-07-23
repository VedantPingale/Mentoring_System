from django.db import models
from django.contrib.auth.models import User

class Certification(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure correct relationship
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='certifications/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
