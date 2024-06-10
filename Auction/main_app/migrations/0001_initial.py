# Generated by Django 5.0.6 on 2024-06-10 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('email', models.CharField(max_length=200)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidder_id', models.CharField(max_length=200)),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.CharField(max_length=200)),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_slug', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=200)),
                ('prodeuct_category', models.CharField(choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Home', 'Home'), ('Sports', 'Sports'), ('Toys', 'Toys')], max_length=200)),
                ('product_date', models.DateTimeField(auto_now_add=True)),
                ('owner_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_date', models.DateTimeField(auto_now_add=True)),
                ('bid_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
            ],
        ),
    ]
