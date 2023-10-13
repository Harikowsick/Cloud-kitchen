# Generated by Django 4.2 on 2023-08-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_ordermodel_city_ordermodel_email_ordermodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='pincode',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
