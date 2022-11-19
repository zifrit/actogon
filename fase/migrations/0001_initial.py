# Generated by Django 4.0 on 2022-11-19 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='photo/%Y/%m.%d/', verbose_name='фото проблемы')),
                ('like', models.IntegerField(verbose_name='количество лайков')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('place', models.CharField(max_length=255, verbose_name='место')),
                ('coordinate', models.CharField(max_length=255, verbose_name='координаты')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fase.events', verbose_name='статья комментария')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.customuser', verbose_name='кто комментатор')),
            ],
        ),
    ]
