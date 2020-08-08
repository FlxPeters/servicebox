# Generated by Django 3.0.6 on 2020-08-07 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0001_initial'),
        ('services', '0006_auto_20200807_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='operator',
            field=models.ForeignKey(help_text='Which tenant operates and runs this service?', on_delete=django.db.models.deletion.PROTECT, related_name='operator', to='tenancy.Tenant'),
        ),
        migrations.AlterField(
            model_name='service',
            name='owner',
            field=models.ForeignKey(help_text='Which tenant owns this service from a bussiness perspective and is responsible for it?', on_delete=django.db.models.deletion.PROTECT, related_name='owner', to='tenancy.Tenant'),
        ),
    ]