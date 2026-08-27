from django.db import models

# Example models for the academics app:

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField(default=40)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name