# Generated by Django 4.1 on 2022-10-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0004_alter_order_options_alter_orderfilling_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='is_hot',
            field=models.BooleanField(default=False),
        ),
    ]
