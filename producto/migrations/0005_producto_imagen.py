# Generated by Django 4.0.2 on 2022-03-03 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_remove_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='productos'),
        ),
    ]
