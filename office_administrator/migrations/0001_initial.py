# Generated by Django 3.1.4 on 2020-12-30 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college_owners', '0001_initial'),
        ('super_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='null', max_length=100)),
                ('lastname', models.CharField(default='null', max_length=100)),
                ('email', models.CharField(default='null', max_length=255)),
                ('password', models.CharField(default='null', max_length=500)),
                ('phone', models.CharField(default='null', max_length=15)),
                ('address', models.TextField(default='null')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='active', max_length=15)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='college_owners.colleges')),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='null', max_length=200)),
                ('description', models.CharField(default='null', max_length=500)),
                ('duration', models.CharField(choices=[('1', '1 Year'), ('2', '2 Year'), ('3', '3 Year'), ('4', '4 Year'), ('5', '5 Year'), ('6', '6 Year'), ('7', '7 Year'), ('8', '8 Year')], default='1', max_length=15)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='college_owners.colleges')),
                ('course_stream', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='super_admin.coursestream')),
                ('course_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='super_admin.coursetype')),
            ],
        ),
    ]