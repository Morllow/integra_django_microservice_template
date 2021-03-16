from django.db import models
from .validators import validate_file_extension


class Data(models.Model):
    name = models.CharField(max_length=200, unique=True)
    template = models.FileField(max_length=128, upload_to='templates/data/', validators=[validate_file_extension])
    data = models.TextField(default='{}')

    def __str__(self):
        return 'Данные: ' + self.name

    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'данные'


class Element(models.Model):
    name = models.CharField(max_length=200, unique=True)
    template = models.FileField(max_length=128, upload_to='templates/elements/', validators=[validate_file_extension])
    depends_in = models.ManyToManyField(Data)

    def __str__(self):
        return 'Элемент: ' + self.name

    class Meta:
        verbose_name = 'Элементы'
        verbose_name_plural = 'Элементы'


class Block(models.Model):
    name = models.CharField(max_length=200, unique=True)
    template = models.FileField(max_length=128, upload_to='templates/blocks/', validators=[validate_file_extension])
    depends_on = models.ManyToManyField(Element)

    def __str__(self):
        return 'Блок: ' + self.name

    class Meta:
        verbose_name = 'Блоки'
        verbose_name_plural = 'Блоки'


class Page(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=64, unique=True, default='Title', verbose_name='Заголовок')
    description = models.CharField(max_length=128, unique=True, default='')
    template = models.FileField(max_length=128, upload_to='templates/pages/', validators=[validate_file_extension],
                                verbose_name='Файл шалона')
    blocks = models.ManyToManyField(Block, verbose_name='Состоит из блоков')

    def __str__(self):
        return 'Страница: ' + self.name

    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'страницы'
