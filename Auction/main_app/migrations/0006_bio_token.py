# Generated by Django 5.0.6 on 2024-06-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_prodeuct_category_product_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='token',
            field=models.CharField(default='1234', max_length=10),
            preserve_default=False,
        ),
    ]
