from django.contrib import admin
from .models import *

class GoodsInline(admin.TabularInline):
    model = Goods  # отбражение товаров прямо в своей группе(клацнуть на нужной группе)
    extra = 0  # кол-во пустых полей

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price','photo', 'is_hot')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    # list_editable = ('is_active',)  # возможность редактирования прямо в таблице
    list_filter = ('goods_group', 'is_hot')  # фильтр для админки
    prepopulated_fields = {"slug": ("name",)}  # автоматическое заполнение поля slug


class GoodsGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    inlines = [GoodsInline]

class OrderFillingInline(admin.TabularInline):
    model = OrderFilling  # отбражение наполнения заказа прямо в самом заказе(клацнуть на нужном заказе)
    extra = 1  # кол-во пустых полей

class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'goods', 'amount', 'price', 'total_price')
    list_display_links = ('id', 'user', 'goods')
    search_fields = ('user', 'goods')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'time_create', 'time_update', 'description', 'is_paid', 'is_active', 'total_price')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'description')
    inlines = [OrderFillingInline]

class OrderFillingAdmin(admin.ModelAdmin):
    list_display = ('goods', 'amount', 'order')
    list_display_links = ('goods', 'order')
    search_fields = ('goods', 'order')


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods', 'user', 'recommendation', 'description')
    list_display_links = ('id', 'goods', 'user')
    search_fields = ('goods', 'user')

admin.site.register(GoodsGroup, GoodsGroupAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderFilling, OrderFillingAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
