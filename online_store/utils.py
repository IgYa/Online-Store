from django.db.models import Count
from django.contrib.auth.models import AbstractUser, User

from .models import *


menu = [{'title': "Про сайт", 'url_name': 'about'},
        {'title': "Інформація", 'url_name': 'info'},
        {'title': "Мій Кошик", 'url_name': 'basket'},
]

# if not User.is_staff:
#     menu2.pop(-2)
#
# menu = menu2



class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        groups = GoodsGroup.objects.all()
        #groups = GoodsGroup.objects.annotate(Count('goods'))  # если товаров в группе нет, то группа не отображается

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(0)
        if self.request.user.is_staff:
            user_menu.append({'title': "Новий товар", 'url_name': 'goods_new'})

        context['menu'] = user_menu
        # context['menu'] = menu
        context['groups'] = groups
        if 'groups_selected' not in context:
            context['groups_id_selected'] = 0
        return context
