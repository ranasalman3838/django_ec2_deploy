from django.db import models

# Create your models here.



from django.db import models
import datetime


class Task(models.Model):
    name = models.CharField(max_length=200, verbose_name='Task Name')
    description = models.TextField(null=True)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
