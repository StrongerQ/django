from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=64,verbose_name='书名') #给列取别名
    price = models.IntegerField(null=True,verbose_name='价格')
    author = models.ManyToManyField("Author")
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE,verbose_name='出版社')

    def __str__(self):
        return self.name
    class Meta: #设置表方法的源类
        unique_together = (('name','price'),) #联合唯一

class Author(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name