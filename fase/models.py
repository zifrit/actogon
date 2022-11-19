from django.db import models
from actogon import settings


class Events(models.Model):
    photo = models.FileField(upload_to='photo/%Y/%m.%d/', verbose_name='фото проблемы')
    like = models.IntegerField(verbose_name='количество лайков', default=0)
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    place = models.CharField(max_length=255, verbose_name='место')
    coordinate = models.CharField(max_length=255, verbose_name='координаты')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'События'
        ordering = ['-like']


class Comments(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='кто комментатор',
                             default=None)
    event = models.ForeignKey(to='Events', on_delete=models.CASCADE, verbose_name='статья комментария')
    text = models.TextField(verbose_name='текст комментария', default=None)

    class Meta:
        db_table = 'Комментарии'


class Likes(models.Model):
    event = models.ForeignKey(to=Events, on_delete=models.CASCADE, verbose_name='событие')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='кто лайкал',
                             default=None)
