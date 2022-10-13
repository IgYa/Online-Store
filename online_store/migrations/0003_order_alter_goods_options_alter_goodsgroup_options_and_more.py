# Generated by Django 4.1 on 2022-10-06 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_store', '0002_remove_goods_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Час зміни')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('is_paid', models.BooleanField(default=True, verbose_name='Оплачений')),
                ('is_active', models.BooleanField(default=False, verbose_name='Скасован')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ('name',), 'verbose_name': 'Канцтовари', 'verbose_name_plural': 'Канцтовари'},
        ),
        migrations.AlterModelOptions(
            name='goodsgroup',
            options={'ordering': ('name',), 'verbose_name': 'Групи канцтоварів', 'verbose_name_plural': 'Групи канцтоварів'},
        ),
        migrations.AlterField(
            model_name='goods',
            name='barcode',
            field=models.CharField(blank=True, max_length=13, verbose_name='штрихкод'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(blank=True, verbose_name='опис'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='online_store.goodsgroup', verbose_name='група'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=200, verbose_name='найменування'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='part_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='код виробника'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='goodsgroup',
            name='description',
            field=models.TextField(blank=True, verbose_name='опис'),
        ),
        migrations.AlterField(
            model_name='goodsgroup',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='найменування'),
        ),
        migrations.CreateModel(
            name='OrderFilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='кількість')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='online_store.goods', verbose_name='Найменування товару')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='online_store.order')),
            ],
        ),
    ]
