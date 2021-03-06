# Generated by Django 3.2.3 on 2022-03-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220319_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Is student'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Is teacher'),
        ),
    ]
