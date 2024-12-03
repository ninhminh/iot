# Generated by Django 5.1.3 on 2024-12-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='wateringschedule',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='wateringschedule',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
