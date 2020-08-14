# Generated by Django 2.2.5 on 2020-08-04 16:21

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20200804_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, max_length=250, null=True, populate_from='title', unique=True, unique_for_date='publish'),
        ),
    ]
