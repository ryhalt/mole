# Generated by Django 2.2.2 on 2021-07-28 17:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0007_scenario_scripts'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityState',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, default='')),
                ('point_style_icon_transform', models.CharField(blank=True, max_length=100, null=True)),
                ('point_style_color_transform', models.CharField(blank=True, max_length=100, null=True)),
                ('point_style_use_marker_pin_override', models.BooleanField(blank=True, default=None, null=True)),
                ('point_style_marker_color_transform', models.CharField(blank=True, max_length=100, null=True)),
                ('point_style_scale_factor_override', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('point_style_animation_transform', models.CharField(blank=True, max_length=100, null=True)),
                ('point_style_render_as_symbol_override', models.BooleanField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='entityeventrole',
            name='valid_entity_groups',
            field=models.ManyToManyField(blank=True, to='data_collection.EntityGroup'),
        ),
        migrations.AddField(
            model_name='entityeventrole',
            name='valid_entity_types',
            field=models.ManyToManyField(blank=True, to='data_collection.EntityType'),
        ),
        migrations.AddField(
            model_name='entityeventrole',
            name='valid_event_types',
            field=models.ManyToManyField(blank=True, to='data_collection.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='invalid_entities',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='entityeventrole',
            name='entity_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_collection.EntityState'),
        ),
    ]
