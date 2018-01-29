from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField(null=True)
    author = models.ManyToManyField("Author")
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)

    class Meta: #设置表方法的源类
        unique_together = (('name','price'),) #联合唯一

class Author(models.Model):
    name = models.CharField(max_length=64)


class Publish(models.Model):
    name = models.CharField(max_length=64)