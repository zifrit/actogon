# Generated by Django 4.0 on 2022-11-20 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fase', '0012_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='photo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fase.photo'),
        ),
    ]