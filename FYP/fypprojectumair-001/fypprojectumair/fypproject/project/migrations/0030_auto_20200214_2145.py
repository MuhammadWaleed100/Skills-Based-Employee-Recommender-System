# Generated by Django 3.0.2 on 2020-02-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0029_auto_20200214_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intoresume',
            name='d_resume_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='d_resume_title',
            field=models.CharField(max_length=50),
        ),
    ]
