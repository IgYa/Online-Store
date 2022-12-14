# Generated by Django 4.1 on 2022-09-28 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
                ('part_number', models.CharField(blank=True, max_length=30)),
                ('barcode', models.CharField(blank=True, max_length=13)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('goods_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='online_store.goodsgroup')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
