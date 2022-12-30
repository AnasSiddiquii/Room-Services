# Generated by Django 4.1.3 on 2022-12-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('contact1', models.CharField(max_length=30, null=True)),
                ('contact2', models.CharField(max_length=30, null=True)),
                ('booking_date', models.CharField(max_length=30, null=True)),
                ('total_days', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
