from django.db import models


class Events(models):
    photo = models.FileField(upload_to='photo/%Y/%m.%d/', verbose_name='фото проблемы')
    like = models.IntegerField(verbose_name='количество лайков')
    whose = models.ForeignKey(to='CustomUser', on_delete=models.CASCADE, verbose_name='чьё событие')
