# Generated by Django 4.2 on 2023-08-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_ordermodel_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
