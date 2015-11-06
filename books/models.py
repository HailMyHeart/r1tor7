from django.db import models



class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 70)
    Age = models.CharField(max_length = 3)
    Country = models.CharField(max_length = 70)

class Book(models.Model):
    ISBN = models.CharField(primary_key=True, max_length = 30)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 100)
    PublishDate = models.CharField(max_length = 11)
    Price = models.CharField(max_length = 10)

# Create your models here.
