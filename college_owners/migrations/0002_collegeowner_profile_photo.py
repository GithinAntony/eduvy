# Generated by Django 3.1.4 on 2021-01-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_owners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegeowner',
            name='profile_photo',
            field=models.TextField(null=True),
        ),
    ]
