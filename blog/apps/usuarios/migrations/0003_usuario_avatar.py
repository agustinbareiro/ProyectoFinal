# Generated by Django 4.2.2 on 2023-07-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(null=True, upload_to='usuarios'),
        ),
    ]
