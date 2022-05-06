# Generated by Django 2.2.2 on 2021-07-09 18:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_collection', '0006_pose_speed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('event_metadata_contains', models.CharField(blank=True, max_length=100, null=True)),
                ('event_metadata_excludes', models.CharField(blank=True, max_length=100, null=True)),
                ('trigger_metadata_contains', models.CharField(blank=True, max_length=100, null=True)),
                ('trigger_metadata_excludes', models.CharField(blank=True, max_length=100, null=True)),
                ('trial_has_event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='script_condition_has_event', to='data_collection.EventType')),
                ('trial_missing_event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='script_condition_missing_event', to='data_collection.EventType')),
            ],
        ),
        migrations.CreateModel(
            name='ScriptedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('conditions_pass_if_any', models.BooleanField(default=False)),
                ('delay_seconds', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('add_event_metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('copy_trigger_metadata', models.BooleanField(default=False)),
                ('conditions', models.ManyToManyField(blank=True, to='automation.ScriptCondition')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scripted_event', to='data_collection.EventType')),
                ('next_scripted_event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scripted_event', to='automation.ScriptedEvent')),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('run_limit', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('auto_repeat_count', models.PositiveIntegerField(default=0)),
                ('conditions_pass_if_any', models.BooleanField(default=False)),
                ('cancelling_event_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cancelling_type', to='data_collection.EventType')),
                ('conditions', models.ManyToManyField(blank=True, related_name='script_conditions', to='automation.ScriptCondition')),
                ('initiating_event_types', models.ManyToManyField(related_name='initiating_types', to='data_collection.EventType')),
                ('scripted_event_head', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='script', to='automation.ScriptedEvent')),
            ],
        ),
        migrations.CreateModel(
            name='ScriptRunCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='script_run_count', to='automation.Script')),
                ('trial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='script_run_count', to='data_collection.Trial')),
            ],
            options={
                'unique_together': {('trial', 'script')},
            },
        ),
    ]
