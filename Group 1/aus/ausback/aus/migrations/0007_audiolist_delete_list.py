# Generated by Django 4.2.5 on 2023-12-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aus', '0006_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='audioList',
            fields=[
                ('list_id', models.IntegerField(primary_key=True, serialize=False)),
                ('list_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='list',
        ),
    ]