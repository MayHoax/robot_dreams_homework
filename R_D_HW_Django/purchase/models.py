from book.models import Book
from django.db import models
from user.models import User


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='purchases', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.book.title}  {self.date}'

    class Meta:
        ordering = ['-date']
