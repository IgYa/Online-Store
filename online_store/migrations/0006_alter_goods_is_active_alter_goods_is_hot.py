# Generated by Django 4.1 on 2022-10-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0005_goods_is_active_goods_is_hot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Актуальний'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='"Гарячий"'),
        ),
    ]
