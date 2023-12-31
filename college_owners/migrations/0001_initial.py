# Generated by Django 3.1.4 on 2020-12-30 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('super_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='collegeOwner',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='null', max_length=100)),
                ('lastname', models.CharField(default='null', max_length=100)),
                ('email', models.CharField(default='null', max_length=255)),
                ('password', models.CharField(default='null', max_length=500)),
                ('phone', models.CharField(default='null', max_length=15)),
                ('address', models.TextField(default='null')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='active', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='colleges',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='null', max_length=200)),
                ('phone', models.CharField(default='null', max_length=15)),
                ('website', models.CharField(default='null', max_length=200)),
                ('email', models.CharField(default='null', max_length=200)),
                ('address', models.TextField(default='null')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='active', max_length=15)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='super_admin.city')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='college_owners.collegeowner')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='super_admin.state')),
            ],
        ),
    ]
