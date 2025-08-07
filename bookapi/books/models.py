from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    isbn = models.CharField(max_length=15, unique=True, null=False)
    published_date = models.DateField()

    def __str__(self):
        return self.title
