# Generated by Django 3.0.3 on 2020-03-31 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0004_customer_no_of_addr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_available',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]