# Generated by Django 2.2 on 2020-08-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0065_recommended_hired'),
    ]

    operations = [
        migrations.CreateModel(
            name='messeges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('msg', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]