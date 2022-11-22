# Generated by Django 4.1.1 on 2022-11-22 11:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_alter_division_description_alter_division_location_and_more'),
        ('vmq', '0005_theme_quality_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmqitem',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='vmqitem',
            name='defer_immediate',
            field=models.CharField(blank=True, choices=[('Deferred', 'Deferred'), ('Immediate', 'Immediate')], default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vmqitem',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.employee'),
        ),
    ]