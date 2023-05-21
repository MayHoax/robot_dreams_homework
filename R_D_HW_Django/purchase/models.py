from user.models import User
from book.models import Book
from django.db import models


class Purchase(models.Model):
    book = models.ForeignKey(Book, related_name='purchases', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        ordering =['-date']
