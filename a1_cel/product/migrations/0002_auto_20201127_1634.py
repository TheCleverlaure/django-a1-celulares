# Generated by Django 3.0 on 2020-11-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('A', 'Audífonos'), ('C', 'Carcasa'), ('VT', 'Vidrio Templado'), ('CM', 'Cosa Magnetica')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
        ),
    ]
