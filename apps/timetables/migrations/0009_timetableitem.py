# Generated by Django 2.2.5 on 2019-09-28 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0008_talk_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='timetables.TimeTableColumn', verbose_name='列')),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='timetables.TimeTableRow', verbose_name='行')),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_item', to='timetables.Talk', verbose_name='トーク')),
            ],
        ),
    ]
