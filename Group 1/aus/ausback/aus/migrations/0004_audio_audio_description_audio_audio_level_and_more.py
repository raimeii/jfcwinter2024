# Generated by Django 4.2.5 on 2023-12-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aus', '0003_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio_description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_level',
            field=models.CharField(default='All levels', max_length=20),
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_type',
            field=models.CharField(default='Undefined', max_length=20),
        ),
    ]