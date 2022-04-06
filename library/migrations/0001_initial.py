# Generated by Django 4.0.1 on 2022-03-31 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('book_sn', models.CharField(max_length=3)),
                ('rented', models.IntegerField(default=0, editable=False)),
                ('book_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.", regex='^\\d{10}$')])),
                ('book_sn', models.CharField(default='', editable=False, max_length=3)),
                ('cost_per_day', models.PositiveIntegerField(default=0, editable=False)),
                ('days_of_rent', models.PositiveIntegerField(default=0, editable=False)),
            ],
        ),
    ]