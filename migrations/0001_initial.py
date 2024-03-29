# Generated by Django 3.2.8 on 2021-10-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='veh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField()),
                ('avgSpeed', models.IntegerField()),
                ('temperature', models.FloatField()),
                ('fuelLevel', models.FloatField()),
                ('EngineStatus', models.TextField(max_length=30)),
                ('cam1', models.TextField(max_length=5)),
                ('cam2', models.TextField(max_length=5)),
            ],
        ),
    ]
