# Generated by Django 4.2.8 on 2023-12-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aus", "0002_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="question",
            fields=[
                ("question_id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]