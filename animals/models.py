from django.db import models


class Animal(models.Model):
    kind = models.CharField('Вид', max_length=200)
    breed = models.CharField('Порода', max_length=200, blank=True)
    name = models.CharField('Имя', max_length=200)
    entry_date = models.DateField('Дата поступления', blank=True)
    weight = models.FloatField('Вес', blank=True)
    height = models.FloatField('Рост', blank=True)
    special_signs = models.TextField()

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
