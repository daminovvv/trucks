# Generated by Django 4.2 on 2023-05-30 11:21

from django.db import migrations, models
import django.db.models.deletion
import trucksapp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=100, unique=True, validators=[trucksapp.validators.validate_postcode])),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(validators=[trucksapp.validators.validate_weight])),
                ('description', models.TextField()),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_cargo', to='trucksapp.location')),
                ('pickup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_cargo', to='trucksapp.location')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, unique=True, validators=[trucksapp.validators.validate_car_number])),
                ('capacity', models.IntegerField(validators=[trucksapp.validators.validate_weight])),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trucksapp.location')),
            ],
        ),
    ]