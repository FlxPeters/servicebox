# Generated by Django 3.0.6 on 2020-08-11 07:12

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenantgroup',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='name', unique=True),
        ),
    ]
