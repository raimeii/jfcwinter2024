# Generated by Django 4.2.5 on 2023-12-14 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aus', '0005_alter_audio_audio_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('list_id', models.IntegerField(primary_key=True, serialize=False)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aus.audio')),
            ],
        ),
    ]