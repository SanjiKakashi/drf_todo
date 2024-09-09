# Generated by Django 5.0.7 on 2024-09-06 14:37

from datetime import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0002_todomodel_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="todomodel",
            name="dueDate",
            field=models.DateTimeField(default=datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="todomodel",
            name="priority",
            field=models.CharField(default="", max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="todomodel",
            name="taskStatus",
            field=models.CharField(default="", max_length=30),
            preserve_default=False,
        ),
    ]
