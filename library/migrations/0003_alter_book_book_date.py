# Generated by Django 4.0.1 on 2022-03-31 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_date',
            field=models.DateField(default=datetime.date(2022, 3, 31)),
        ),
    ]