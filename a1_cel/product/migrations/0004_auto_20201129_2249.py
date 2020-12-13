# Generated by Django 3.0 on 2020-11-30 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201127_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.CharField(default='..\\static_in_env\\img\no-photo-available.png', max_length=2083),
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]