# Generated by Django 4.1.5 on 2023-01-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
