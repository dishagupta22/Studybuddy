# Generated by Django 3.2.6 on 2021-08-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateTimeField(),
        ),
    ]
