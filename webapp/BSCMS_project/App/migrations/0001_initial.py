# Generated by Django 4.1.3 on 2022-11-24 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BabySitters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobileNo', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('languagesKnown', models.TextField(null=True)),
                ('babySittersExp', models.CharField(max_length=100, null=True)),
                ('profilePic', models.ImageField(height_field='200px', null=True, upload_to='', width_field='200px')),
                ('certificate', models.CharField(max_length=300, null=True)),
                ('descreption', models.TextField(null=True)),
                ('regDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('massege', models.TextField(null=True)),
                ('enquiryDate', models.DateField(auto_now=True)),
                ('isRead', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollNumber', models.IntegerField(max_length=10, null=True)),
                ('yourName', models.CharField(max_length=100, null=True)),
                ('phoneNumber', models.IntegerField(null=True)),
                ('alternateNumber', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('childName', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('childGender', models.CharField(max_length=10, null=True)),
                ('programName', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('landmark', models.CharField(max_length=300, null=True)),
                ('enrollmentDate', models.DateTimeField(auto_now=True, null=True)),
                ('remark', models.CharField(max_length=400, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('remarkDate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100, null=True)),
                ('serviceDetail', models.CharField(max_length=100, null=True)),
                ('creationsDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('dateOfSub', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppAdmin_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminMobile', models.IntegerField(null=True)),
                ('registerDate', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
