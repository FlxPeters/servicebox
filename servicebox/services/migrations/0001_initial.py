# Generated by Django 3.0.6 on 2020-05-27 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('platforms', '0001_initial'),
        ('tenancy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Unique name of the service', max_length=200, unique=True)),
                ('configration_management', models.URLField(blank=True, help_text='Link to the source code and configuration management of the service.', null=True)),
                ('documentation', models.URLField(blank=True, help_text='Link to the service docs. For example a Wiki page. ', null=True)),
                ('business_overview', models.TextField(blank=True, help_text='What business need is met by this service or system? What expectations do we have about availability and performance?', null=True)),
                ('technical_overview', models.TextField(blank=True, help_text='What kind of system is this', null=True)),
                ('sla', models.CharField(blank=True, help_text='What explicit or implicit expectations are there from users or clients about the availability of the service or system?', max_length=200, null=True)),
                ('hours_of_operation', models.CharField(blank=True, help_text='During what hours does the service or system actually need to operate? Can portions or features of the system be unavailable at times if needed?', max_length=200, null=True)),
                ('components', models.TextField(blank=True, help_text='Which distinct software applications, daemons, services, etc. make up the service or system?', null=True)),
                ('depends_on', models.ManyToManyField(blank=True, help_text='What external dependencies does the service have?', to='services.Service')),
                ('owner', models.ForeignKey(blank=True, help_text='Which team owns and runs this service or system?', null=True, on_delete=django.db.models.deletion.PROTECT, to='tenancy.Tenant')),
                ('platform', models.ForeignKey(blank=True, help_text='Platform the service is running on', null=True, on_delete=django.db.models.deletion.PROTECT, to='platforms.Platform')),
            ],
        ),
    ]
