from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    # path('index', index, name='index'),
    path('about/', about, name='about'),
    path('basket/', basket, name='basket'),  #
    path('add_basket/', add_basket, name='add_basket'),  #<int:g_id>/
    path('goods/', GoodsHome.as_view(), name='goods_show'),  # goods_show
    path('goods_new/', goods_new, name='goods_new'),
    path('goods_id/<int:g_id>/', goods_id, name='goods_id'),
    path('groups_id/<int:group_id>/', groups_id, name='groups_id'),  # groups_id
    #path('groups/<slug:group>/', name='groups_slug'),
    path('info/', info, name='info'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    #path('product_review/<int:g_id>/', product_review, name='product_review'),
    path('product_review/', product_review, name='product_review'),

    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    # re_path(r'^archive_red/(?P<year>[0-9]{4})/', archive_red),
]
