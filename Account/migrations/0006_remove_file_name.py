# Generated by Django 4.0 on 2021-12-12 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]
