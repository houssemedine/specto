# Generated by Django 4.1.1 on 2022-11-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VmqKPI_dateRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_stop', models.DateField()),
            ],
        ),
    ]
