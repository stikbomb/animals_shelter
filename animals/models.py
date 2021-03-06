from django.db import models
from softdelete.models import SoftDeleteObject


class Animal(SoftDeleteObject, models.Model):
    kind = models.CharField('Вид', max_length=200)
    breed = models.CharField('Порода', max_length=200, blank=True, null=True)
    name = models.CharField('Имя', max_length=200)
    entry_date = models.DateField('Дата поступления', blank=True, null=True)
    weight = models.FloatField('Вес', blank=True, null=True)
    height = models.FloatField('Рост', blank=True, null=True)
    special_signs = models.TextField('Особые приметы', blank=True)

    def __str__(self):
        return f"{self.kind} по кличке {self.name}"


class Image(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='images', verbose_name='Животное')
    image = models.ImageField('Картинка')
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f"{self.position} {self.animal}"
