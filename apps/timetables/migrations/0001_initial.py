# Generated by Django 2.2.5 on 2019-09-14 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('speaker_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('talk_language', models.CharField(max_length=100)),
                ('slide_language', models.CharField(max_length=100)),
                ('target_audience', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=False)),
                ('slug', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTableColumn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetables.TimeTable')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTableRow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetables.TimeTable')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTableItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_empty', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('column_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetables.TimeTableColumn')),
                ('row_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetables.TimeTableRow')),
                ('talk_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetables.Talk')),
            ],
        ),
    ]
