# Generated by Django 2.2.2 on 2020-11-11 00:07

import data_collection.models
import datetime
from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('trial_id_major_name', models.CharField(blank=True, default='', max_length=100)),
                ('trial_id_minor_name', models.CharField(blank=True, default='', max_length=100)),
                ('trial_id_micro_name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['-start_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('display_name', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CapabilityUnderTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ConditionVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('variable', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='DataManipulator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('module', models.CharField(max_length=100)),
                ('method_name', models.CharField(max_length=100)),
                ('parameters', models.CharField(blank=True, max_length=255)),
                ('dataset', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('display_name', models.CharField(blank=True, default='', max_length=100)),
                ('physical_id', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EntityGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('basemap_element', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(editable=False)),
                ('submitted_datetime', models.DateTimeField(auto_now_add=True)),
                ('start_datetime', models.DateTimeField(blank=True)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'ordering': ['-start_datetime'],
            },
        ),
        migrations.CreateModel(
            name='EventLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('visibility', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('has_duration', models.BooleanField(default=False)),
                ('ends_segment', models.BooleanField(default=False)),
                ('is_manual', models.BooleanField(default=True)),
                ('priority_metadata', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None)),
                ('metadata_style_fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('event_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.EventLevel')),
                ('exclusive_with', models.ManyToManyField(blank=True, related_name='_eventtype_exclusive_with_+', to='data_collection.EventType')),
            ],
        ),
        migrations.CreateModel(
            name='ExtractionField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('label', models.CharField(max_length=255)),
                ('field_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExtractionSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('extraction_fields', models.ManyToManyField(to='data_collection.ExtractionField')),
            ],
        ),
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='report_figures/')),
                ('generated_datetime', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='FigureFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('method_name', models.CharField(max_length=100)),
                ('module', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FigureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('parameters', models.CharField(blank=True, max_length=255)),
                ('prefix', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('data_manipulator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.DataManipulator')),
                ('figure_family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.FigureFamily')),
            ],
        ),
        migrations.CreateModel(
            name='ImageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('topic', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IteratedDataManipulator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('prefix', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('data_manipulator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.DataManipulator')),
            ],
        ),
        migrations.CreateModel(
            name='IteratedExtractionSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('prefix', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('extraction_spec', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.ExtractionSpecification')),
            ],
        ),
        migrations.CreateModel(
            name='Iterator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('extraction_spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.ExtractionSpecification')),
                ('unique_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.ExtractionField')),
            ],
        ),
        migrations.CreateModel(
            name='KeyValuePair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('timezone', models.CharField(blank=True, default='America/Los_Angeles', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrderedTriggerResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order', 'trigger_response'],
            },
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PointStyle',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('use_marker_pin', models.BooleanField(default=True)),
                ('marker_color', models.CharField(blank=True, max_length=100, null=True)),
                ('scale_factor', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('animation', models.CharField(blank=True, max_length=100, null=True)),
                ('render_as_symbol', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PoseSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='QuerySetMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('method_name', models.CharField(max_length=100)),
                ('parameters', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuerySetSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('model_name', models.CharField(max_length=100)),
                ('methods', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RequestedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('destination_url', models.TextField(default='')),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('variant', models.CharField(blank=True, max_length=100, null=True)),
                ('time_limit', models.DurationField(blank=True, default=datetime.timedelta, null=True)),
                ('entity_groups', models.ManyToManyField(blank=True, related_name='scenarios', to='data_collection.EntityGroup')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenarios', to='data_collection.Location')),
            ],
        ),
        migrations.CreateModel(
            name='ServerParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('param', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('key', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('capabilities_under_test', models.ManyToManyField(to='data_collection.CapabilityUnderTest')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TestCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['role', 'user'],
                'unique_together': {('user', 'role')},
            },
        ),
        migrations.CreateModel(
            name='TestMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('version_major', models.IntegerField()),
                ('version_minor', models.IntegerField()),
                ('version_micro', models.IntegerField()),
                ('has_segments', models.BooleanField(default=False)),
                ('variant', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('current', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TriggerResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('method', models.CharField(max_length=100)),
                ('module', models.CharField(max_length=100)),
                ('parameters', models.ManyToManyField(blank=True, to='data_collection.KeyValuePair')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('is_active', models.BooleanField(default=True)),
                ('is_manual', models.BooleanField(default=False)),
                ('creates_event', models.BooleanField(default=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('trigger_transport', models.CharField(blank=True, default='', max_length=10)),
                ('condition_variables', models.ManyToManyField(blank=True, to='data_collection.ConditionVariable')),
                ('event_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.EventType')),
                ('requested_dataset', models.ManyToManyField(blank=True, to='data_collection.RequestedData')),
                ('trigger_responses', models.ManyToManyField(blank=True, to='data_collection.OrderedTriggerResponse')),
            ],
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_major', models.IntegerField()),
                ('id_minor', models.IntegerField()),
                ('id_micro', models.IntegerField()),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('bagfile', models.CharField(blank=True, default='', max_length=100)),
                ('note', models.TextField(blank=True, default='')),
                ('current', models.BooleanField(default=False)),
                ('reported', models.BooleanField(default=True)),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trials', to='data_collection.Campaign')),
                ('entities', models.ManyToManyField(blank=True, related_name='trials', to='data_collection.Entity')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trials', to='data_collection.Scenario')),
                ('system_configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.SystemConfiguration')),
                ('test_condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trials', to='data_collection.TestCondition')),
                ('testers', models.ManyToManyField(to='data_collection.Tester')),
            ],
            options={
                'ordering': ['id_major', 'id_minor', 'id_micro'],
                'unique_together': {('id_major', 'id_minor', 'id_micro', 'campaign')},
            },
        ),
        migrations.AddField(
            model_name='testcondition',
            name='weather',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_conditions', to='data_collection.Weather'),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('base_url', models.CharField(max_length=1000)),
                ('server_params', models.ManyToManyField(blank=True, to='data_collection.ServerParam')),
                ('server_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.ServerType')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('scenarios', models.ManyToManyField(related_name='potential_segments', to='data_collection.Scenario')),
            ],
        ),
        migrations.AddField(
            model_name='scenario',
            name='test_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenarios', to='data_collection.TestMethod'),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('template', models.FileField(upload_to=data_collection.models.report_templates_path)),
                ('rendered_template', models.FileField(editable=False, upload_to=data_collection.models.rendered_report_templates_path)),
                ('online_report', models.FileField(upload_to=data_collection.models.online_report_path)),
                ('report_archive', models.FileField(upload_to=data_collection.models.report_archive_path)),
                ('modified_datetime', models.DateTimeField(editable=False)),
                ('format', models.CharField(blank=True, choices=[('pdf', '.pdf'), ('html', '.html')], default='.html', max_length=100)),
                ('status', models.CharField(editable=False, max_length=100)),
                ('figure_types', models.ManyToManyField(blank=True, to='data_collection.FigureType')),
                ('iterated_data_manipulators', models.ManyToManyField(blank=True, to='data_collection.IteratedDataManipulator')),
                ('iterated_extraction_specs', models.ManyToManyField(blank=True, to='data_collection.IteratedExtractionSpecification')),
                ('iterators', models.ManyToManyField(blank=True, to='data_collection.Iterator')),
            ],
        ),
        migrations.CreateModel(
            name='Pose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('elevation', models.FloatField(blank=True, null=True)),
                ('heading', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poses', to='data_collection.Entity')),
                ('pose_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.PoseSource')),
            ],
        ),
        migrations.AddField(
            model_name='orderedtriggerresponse',
            name='trigger_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.TriggerResponse'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='data_collection.Event')),
                ('tester', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Tester')),
            ],
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('display_name', models.CharField(blank=True, default='', max_length=100)),
                ('capabilities', models.ManyToManyField(blank=True, related_name='mods_providing', to='data_collection.Capability')),
            ],
        ),
        migrations.AddField(
            model_name='iteratedextractionspecification',
            name='iterator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Iterator'),
        ),
        migrations.AddField(
            model_name='iterateddatamanipulator',
            name='iterator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Iterator'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=data_collection.models.get_unique_image_file_path)),
                ('timestamp', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='data_collection.Event')),
                ('image_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.ImageType')),
            ],
            options={
                'ordering': ['-image_type__id'],
            },
        ),
        migrations.AddField(
            model_name='figuretype',
            name='iterator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Iterator'),
        ),
        migrations.AddField(
            model_name='extractionspecification',
            name='queryset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.QuerySetSpecification'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='point_style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_types_styled', to='data_collection.PointStyle'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='resets_with',
            field=models.ManyToManyField(blank=True, related_name='_eventtype_resets_with_+', to='data_collection.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='segment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Segment'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_pose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='data_collection.Pose'),
        ),
        migrations.AddField(
            model_name='event',
            name='trial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.Trial'),
        ),
        migrations.AddField(
            model_name='event',
            name='trigger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Trigger'),
        ),
        migrations.AddField(
            model_name='event',
            name='weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.Weather'),
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('display_name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('capabilities', models.ManyToManyField(blank=True, related_name='entity_types_posessing', to='data_collection.Capability')),
                ('point_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entity_types_styled', to='data_collection.PointStyle')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='entity',
            name='entity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='data_collection.EntityType'),
        ),
        migrations.AddField(
            model_name='entity',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='related_entities', to='data_collection.EntityGroup'),
        ),
        migrations.AddField(
            model_name='entity',
            name='mods',
            field=models.ManyToManyField(blank=True, related_name='entities_installed', to='data_collection.Mod'),
        ),
        migrations.AddField(
            model_name='capabilityundertest',
            name='performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_collection.Performer'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='orderedtriggerresponse',
            unique_together={('order', 'trigger_response')},
        ),
    ]