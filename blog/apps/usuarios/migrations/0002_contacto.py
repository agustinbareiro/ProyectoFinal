# Generated by Django 4.2.2 on 2023-07-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=40)),
                ('texto', models.TextField()),
            ],
        ),
    ]
