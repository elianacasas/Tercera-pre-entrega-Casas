# Generated by Django 4.2.5 on 2023-10-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_delete_cafeterias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafeterias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('horario', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]