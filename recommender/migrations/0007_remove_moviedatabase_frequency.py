# Generated by Django 3.0.8 on 2020-08-07 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0006_auto_20200807_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedatabase',
            name='frequency',
        ),
    ]
