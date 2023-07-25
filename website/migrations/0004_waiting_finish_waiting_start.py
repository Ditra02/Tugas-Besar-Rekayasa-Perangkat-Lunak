# Generated by Django 4.1.5 on 2023-07-14 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_table_finish'),
    ]

    operations = [
        migrations.AddField(
            model_name='waiting',
            name='finish',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AddField(
            model_name='waiting',
            name='start',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
