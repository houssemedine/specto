# Generated by Django 4.1.1 on 2022-09-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmq', '0002_alter_item_name_alter_vmq_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(default='Theme name', max_length=100),
        ),
    ]
