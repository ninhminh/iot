# Generated by Django 5.1.3 on 2024-12-02 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entity', '0002_alter_device_created_at_alter_device_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateringschedule',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watering_schedules', to='Entity.sensordata'),
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='device',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='sensor_type',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='value',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='soil_moisture',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='Entity.user'),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='water_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
