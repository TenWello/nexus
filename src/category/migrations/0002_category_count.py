# Generated by Django 5.1.7 on 2025-04-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
