# Generated by Django 4.1.3 on 2022-11-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_enrollment_enrollnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='country',
        ),
        migrations.AlterField(
            model_name='babysitters',
            name='profilePic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
