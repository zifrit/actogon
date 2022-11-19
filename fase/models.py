from django.db import models
from back.models import *


class Events(models):
    photo = models.FileField(upload_to='photo/%Y/%m.%d/', verbose_name='фото проблемы')
    like = models.IntegerField(verbose_name='количество лайков')
    whose = models.ForeignKey(to='CustomUser', on_delete=models.CASCADE, verbose_name='чьё событие')
    place = models.CharField(max_length=255, verbose_name='место')
    coordinate = models.CharField(max_length=255, verbose_name='координаты')
    state = models.CharField(max_length=2)


class Comments(models):
    user = models.ForeignKey(to='CustomUser', on_delete=models.CASCADE, verbose_name='кто комментатор')
    event = models.ForeignKey(to='Events', on_delete=models.CASCADE, verbose_name='статья комментария')

