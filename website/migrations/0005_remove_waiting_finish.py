# Generated by Django 4.2.3 on 2023-07-15 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_waiting_finish_waiting_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waiting',
            name='finish',
        ),
    ]
