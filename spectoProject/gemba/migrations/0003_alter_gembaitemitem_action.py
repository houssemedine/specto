# Generated by Django 4.1.1 on 2022-10-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemba', '0002_alter_gembaitemitem_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gembaitemitem',
            name='action',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
