# Generated by Django 2.1 on 2019-12-22 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-create_time']},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]