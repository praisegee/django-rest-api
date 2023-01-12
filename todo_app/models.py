from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title