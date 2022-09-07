# Generated by Django 4.1 on 2022-09-07 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default='Default User', max_length=50)),
                ('updated_by', models.CharField(default='Default User', max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.CharField(blank=True, max_length=50, null=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
                ('restored_by', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(default='Theme name', max_length=30)),
                ('description', models.TextField(default='Theme description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default='Default User', max_length=50)),
                ('updated_by', models.CharField(default='Default User', max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.CharField(blank=True, max_length=50, null=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
                ('restored_by', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(default='Item name', max_length=30)),
                ('description', models.TextField(default='Item description')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vmq.theme')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]