# Generated by Django 4.2.7 on 2023-11-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menu_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.PositiveIntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.IntegerField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
