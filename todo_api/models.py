from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    date_creation = models.DateField(auto_now_add=True)
    flag_due = models.BooleanField()
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
