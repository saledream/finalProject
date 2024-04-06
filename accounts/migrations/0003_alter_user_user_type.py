# Generated by Django 5.0.3 on 2024-03-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor'), ('department head', 'department head')], default='student', max_length=20),
        ),
    ]