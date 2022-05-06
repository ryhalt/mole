# Generated by Django 2.2.2 on 2021-07-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
        ('data_collection', '0006_pose_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='scripts',
            field=models.ManyToManyField(blank=True, related_name='scenarios', to='automation.Script'),
        ),
    ]
