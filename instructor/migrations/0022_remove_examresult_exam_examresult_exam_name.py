# Generated by Django 5.0.3 on 2024-04-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0021_rename_examstatus_modelexamstatus_testexamstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examresult',
            name='exam',
        ),
        migrations.AddField(
            model_name='examresult',
            name='exam_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
