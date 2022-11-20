from django.db import models
from actogon import settings


class Events(models.Model):
    photo = models.ForeignKey(to='Photo', on_delete=models.SET_NULL, null=True, default=None, blank=True)
    like = models.IntegerField(verbose_name='количество лайков', default=0, blank=True)
    title = models.CharField(max_length=255, verbose_name='название', blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    place = models.CharField(max_length=255, verbose_name='место', blank=True)
    coordinate = models.CharField(max_length=255, verbose_name='координаты', blank=True)
    district = models.ForeignKey(to='District', on_delete=models.SET_NULL, null=True, default=None, blank=True)
    STATUS = (
        ('A', 'Принятый'),
        ('S', 'Принял'),
        ('R', 'Отказано'),
        ('T', 'Архив'),
    )
    status = models.CharField(max_length=1, verbose_name='статус', default='F', choices=STATUS)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'События'
        ordering = ['-like']


class Photo(models.Model):
    name = models.FileField(upload_to='photo/%Y/%m.%d/', verbose_name='фото проблемы', blank=True)

    def __str__(self):
        return str(self.name.url)


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

    class Meta:
        db_table = 'Лайки'


class District(models.Model):
    name = models.CharField(max_length=255, verbose_name='район')

    class Meta:
        db_table = 'Районы'
