# Generated by Django 4.0 on 2022-11-19 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
        ('fase', '0002_remove_comments_user_comments_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='back.customuser', verbose_name='кто комментатор'),
        ),
    ]