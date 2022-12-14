# Generated by Django 4.1.2 on 2022-11-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_restaurant_images_delete_postimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('numGuests', models.IntegerField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('rest_id', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
