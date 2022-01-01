# Generated by Django 4.0 on 2021-12-31 07:29

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0003_remove_option_created_remove_option_updated_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="option",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="option",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="option",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("dc1c77d4-ede9-4f4c-8008-70639bc00e58"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("dc1c77d4-ede9-4f4c-8008-70639bc00e58"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("dc1c77d4-ede9-4f4c-8008-70639bc00e58"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]