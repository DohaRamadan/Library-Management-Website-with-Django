# Generated by Django 3.2.4 on 2021-07-12 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rented_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]