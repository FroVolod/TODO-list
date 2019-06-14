from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField(auto_now_add=True)
    flag_due = models.BooleanField()

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
