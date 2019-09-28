# Generated by Django 2.2.5 on 2019-09-28 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0007_talk'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='talks', to='timetables.TimeTable', verbose_name='所属タイムテーブル'),
        ),
    ]
