# Generated by Django 4.1.1 on 2022-10-21 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
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
                ('name', models.CharField(default='Division name', max_length=30)),
                ('location', models.CharField(default='Tunis', max_length=30)),
                ('description', models.CharField(default='Division description', max_length=200)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.IntegerField(unique=True)),
                ('names', models.CharField(max_length=100)),
                ('i_p', models.CharField(max_length=2)),
                ('code', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('wording', models.CharField(max_length=100)),
                ('cost_center', models.CharField(max_length=30)),
                ('job_bulletin', models.CharField(max_length=100)),
                ('resp_matricule_n1', models.IntegerField()),
                ('resp_names_n1', models.CharField(max_length=100)),
                ('resp_matricule_n2', models.IntegerField()),
                ('resp_names_n2', models.CharField(max_length=100)),
                ('staff_tab_afs', models.CharField(max_length=50)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.division')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_data_file', models.FileField(upload_to='configuration/handle_uploaded_file')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
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
                ('name', models.CharField(default='Product name', max_length=30)),
                ('description', models.CharField(default='Product description', max_length=200)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Workshop',
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
                ('name', models.CharField(default='Workshop name', max_length=30)),
                ('description', models.CharField(default='Workshop description', max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.product')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VMS_Planning',
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
                ('month', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('closed', models.BooleanField(default=False)),
                ('vms_employee_qualified', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vms_employee_qualified', to='configuration.employee', to_field='matricule')),
                ('vms_employee_visited', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vms_employee_visited', to='configuration.employee', to_field='matricule')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VMQ_Planning',
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
                ('month', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('closed', models.BooleanField(default=False)),
                ('vmq_employee_qualified', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vmq_employee_qualified', to='configuration.employee', to_field='matricule')),
                ('vmq_employee_visited', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vmq_employee_visited', to='configuration.employee', to_field='matricule')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qualification',
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
                ('vms_qualification', models.BooleanField(default=False)),
                ('vmq_qualification', models.BooleanField(default=False)),
                ('fives_qualification', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(db_column='employee', on_delete=django.db.models.deletion.CASCADE, to='configuration.employee', to_field='matricule')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
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
                ('name', models.CharField(default='Program name', max_length=30)),
                ('description', models.CharField(default='Program description', max_length=200)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.division')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.program'),
        ),
        migrations.AddField(
            model_name='employee',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.product'),
        ),
        migrations.AddField(
            model_name='employee',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.program'),
        ),
        migrations.AddField(
            model_name='employee',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.workshop'),
        ),
    ]
