# Generated by Django 4.2.5 on 2024-01-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aus', '0014_remove_listcontent_id_listcontent_audio_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listcontent',
            name='content_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]