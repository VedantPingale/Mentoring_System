from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='assignment_files/', blank=True, null=True)
    image = models.ImageField(upload_to='assignments/', blank=True, null=True)
    due_date = models.DateTimeField(default='2000-01-01')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_assignments')

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    feedback = models.TextField(blank=True, null=True)
    graded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.submission.student.username} - {self.submission.assignment.title} - {self.score}"
