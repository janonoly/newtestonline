# Generated by Django 2.0.2 on 2020-02-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0007_auto_20200213_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperlist',
            name='jd_choice_num',
            field=models.IntegerField(default=0, verbose_name='多选题数'),
        ),
        migrations.AddField(
            model_name='paperlist',
            name='jd_choice_score',
            field=models.IntegerField(default=0, verbose_name='多选分值'),
        ),
    ]
