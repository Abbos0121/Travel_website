# Generated by Django 4.2.4 on 2023-08-16 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls_new', '0011_carbooking_touristplace_bookings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristplace',
            name='bookings',
        ),
        migrations.DeleteModel(
            name='CarBooking',
        ),
    ]
