# Generated by Django 4.2.4 on 2023-08-02 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0002_task_end_date_task_start_date_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 22, 43, 48, 491307)),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 22, 43, 48, 491307)),
        ),
    ]
