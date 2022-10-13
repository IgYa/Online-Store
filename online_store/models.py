from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save

# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here
#
#     def __str__(self):
#         return self.username


class GoodsGroup(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='найменування')
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name='опис')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups_id', kwargs={'group_id': self.pk})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Групи канцтоварів'  # для отображения в админпанели
        verbose_name_plural = 'Групи канцтоварів'  # это множественное число


# models.ImageField - Требуется библиотека Pillow https://pillow.readthedocs.io/en/latest/
# settings.py - добавить MEDIA_ROOT, MEDIA_URL
# urls.py :
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
class Goods(models.Model):
    name = models.CharField(max_length=200, verbose_name='найменування')
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")
    goods_group = models.ForeignKey(GoodsGroup, on_delete=models.PROTECT, verbose_name='група')
    part_number = models.CharField(max_length=30, blank=True, verbose_name='код виробника')
    barcode = models.CharField(max_length=13, blank=True, verbose_name='штрихкод')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='ціна')
    # discount = models.IntegerField(default=0, verbose_name='Знижка')
    description = models.TextField(blank=True, verbose_name='опис')
    is_active = models.BooleanField(default=True, verbose_name='Актуальний')
    is_hot = models.BooleanField(default=False, verbose_name='"Гарячий"')  # label='Відображається на домашній сторінці сайту'
    photo = models.ImageField(upload_to='', blank=True, null=True, verbose_name='фото')

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}грн'

    # def get_absolute_url(self):
    #     return reverse('goods_id', kwargs={'goods_id': self.pk})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Канцтовари'  # для отображения в админпанели
        verbose_name_plural = 'Канцтовари'  # это множественное число


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Клієнт')
    goods = models.ForeignKey(Goods, on_delete=models.PROTECT, verbose_name='Найменування товару')
    amount = models.IntegerField(default=1, verbose_name='Кількість')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Ціна')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сума')

    def __str__(self):
        return f'{self.user}, {self.goods}, {self.amount}, {self.price}грн'

    # для текущей функции переопределяем метод save()
    def save(self, *args, **kwargs):
        price = self.goods.price
        self.price = price
        self.total_price = self.amount * price

        super(Basket, self).save(*args, **kwargs)


    class Meta:
        ordering = ('user', 'goods')
        verbose_name = 'Кошик'  # для отображения в админпанели
        verbose_name_plural = 'Кошики'  # это множественное число

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сума заказу')  # Общая сумма всех total_price по позициям
    # discount = models.IntegerField(default=0, verbose_name='Знижка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час зміни")
    description = models.TextField(blank=True, verbose_name='Опис')
    is_paid = models.BooleanField(default=False, verbose_name="Оплачений")
    is_active = models.BooleanField(default=False, verbose_name="Скасован")

    def __str__(self):
        return f'№{self.id}, {self.user}, {self.total_price}, {self.description}'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Замовлення'  # для отображения в админпанели Замовлення наповнення
        verbose_name_plural = 'Замовлення'  # это множественное число

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class OrderFilling(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.PROTECT, verbose_name='Найменування товару')
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    amount = models.IntegerField(default=1, verbose_name='кількість')
    price_selling = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Ціна продажу')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сума продажу')  # amount*price_selling

    def __str__(self):
        return f'{self.order}, {self.goods}, {self.amount}'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Замовлення-наповнення'  # для отображения в админпанели Замовлення наповнення
        verbose_name_plural = 'Замовлення-наповнення'  # это множественное число

    # stackoverflow.com/guestions/4269605/django-override-save-for-model
    # для текущей функции переопределяем метод save()
    def save(self, *args, **kwargs):
        price_selling = self.goods.price
        self.price_selling = price_selling
        self.total_price = self.amount * price_selling

        super(OrderFilling, self).save(*args, **kwargs)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    goods = models.ForeignKey(Goods, on_delete=models.PROTECT, verbose_name='Найменування товару')
    recommendation = models.BooleanField(default=True, verbose_name="Рекомендую!")
    description = models.TextField(blank=True, verbose_name='Відгук')

    def __str__(self):
        return f'{self.user}, {self.goods}, {self.recommendation}'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Відгук про товар'  # для отображения в админпанели Замовлення наповнення
        verbose_name_plural = 'Відгуки про товари'  # это множественное число



def goods_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_goods_in_order = OrderFilling.objects.filter(order=order)

    order_total_price = 0
    for item in all_goods_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

# функция post_save, применяем не для модели OrderFilling (иначе будет зацикливание) - расчет суммы заказа
post_save.connect(goods_in_order_post_save, sender=OrderFilling)

