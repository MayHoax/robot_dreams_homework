from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.age}"
