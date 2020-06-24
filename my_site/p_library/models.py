from django.db import models


class Publishing(models.Model):
 # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(db_column='ISBN', max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, models.DO_NOTHING)
    price = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    copy_count = models.SmallIntegerField(blank=True, null=True)
    publishing = models.ForeignKey(
        Publishing,  models.DO_NOTHING, related_name='publish', null=True)

    def __str__(self):
        return self.title
