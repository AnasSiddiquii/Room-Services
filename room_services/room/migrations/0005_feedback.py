# Generated by Django 4.1.3 on 2022-12-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_booking_dob_booking_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=40, null=True)),
                ('contact', models.CharField(max_length=20, null=True)),
                ('comment', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]