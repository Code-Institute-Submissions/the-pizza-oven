# Generated by Django 3.2.7 on 2021-10-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_table'),
        ('bookings', '0002_alter_booking_special_requirements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='tables',
            field=models.ManyToManyField(related_name='bookings', to='restaurant.Table'),
        ),
    ]
