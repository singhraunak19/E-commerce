# Generated by Django 4.2.16 on 2024-09-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Store", "0007_order_address_order_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.BooleanField(default=False),
        ),
    ]