# Generated by Django 4.0 on 2021-12-30 00:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="option",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("054522f9-604f-4a9f-aecf-377a169032ea"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="option",
            name="text",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("054522f9-604f-4a9f-aecf-377a169032ea"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("054522f9-604f-4a9f-aecf-377a169032ea"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
