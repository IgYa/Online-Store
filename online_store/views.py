from decimal import Decimal

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .utils import *
from .forms import *


def home(request: HttpRequest) -> HttpResponse:
    goods_hot = Goods.objects.filter(is_hot=True)
    groups = GoodsGroup.objects.all()
    user = request.user
    context = {
            'user': user,
            'goods_hot': goods_hot,
            'groups': groups,
            # 'groups_id_selected': 0,
            'menu': menu,
            'title': 'Канцтовари - Головна'
    }
    return render(request, 'online_store/home.html', context=context)

class GoodsHome(DataMixin, ListView):
    model = Goods
    template_name = 'online_store/goods.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Канцтовари")
        return dict(list(context.items()) + list(c_def.items()))
        # groups = GoodsGroup.objects.all()
        # context['groups'] = groups
        # context['menu'] = menu
        # context['title'] = 'Канцтовари'
        # context['groups_id_selected'] = 0
        #return context

    # def get_queryset(self):
    #     return Goods.objects.filter(is_active=True)

# def goods_show(request):
#     goods = Goods.objects.all()
#     groups = GoodsGroup.objects.all()
#
#     context = {
#         'goods': goods,
#         'groups': groups,
#         'groups_id_selected': 0,
#         'menu': menu,
#         'title': 'Канцтовари'
#     }
#
#     return render(request, 'online_store/goods.html', context=context)

# def index(request):
#     groups = GoodsGroup.objects.all()
#
#     context = {
#         'groups': groups,
#         'groups_selected': 0,
#         'menu': menu,
#         'title': 'Канцтовари'
#     }
#
#     return render(request, 'online_store/index.html', context=context)


def groups_id(request: HttpRequest, group_id: int) -> HttpResponse:
    goods = Goods.objects.filter(goods_group=group_id)
    groups = GoodsGroup.objects.all()
    title = GoodsGroup.objects.get(id=group_id)

    # Если в группе нет товаров, то вызываем ошибку 404
    if len(goods) == 0:
        raise Http404()

    context = {
        'goods': goods,
        'groups': groups,
        'goods_group': group_id,
        'goods_selected': 0,
        'menu': menu,
        'title': title.name,
        'groups_selected': group_id,
    }

    return render(request, 'online_store/goods.html', context=context)



def goods_id(request: HttpRequest, g_id: int) -> HttpResponse:
    goods = get_object_or_404(Goods, pk=g_id)
    user = request.user
    #goods = Goods.objects.get(id=g_id)
    groups = GoodsGroup.objects.all()

    # Если в группе нет товаров, то вызываем ошибку 404
    # if len(goods) == 0:
    #     raise Http404()

    context = {
        'goods': goods,
        'groups': groups,
        'user': user,
        'menu': menu,
        'title': goods.name,
        'groups_selected': goods.goods_group_id,
    }
    # print(goods)
    # print(goods.goods_group)
    # print(groups)

    return render(request, 'online_store/getgoods.html', context=context)


def groups_slug(request: HttpRequest, group: str) -> HttpResponse:
    return HttpResponse(f"<h1>Групи товарів</h1><p>{group}</p>")


def page_not_found(request: HttpRequest, exception) -> HttpResponse:
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")

# @login_required
def about(request: HttpRequest) -> HttpResponse:
    groups = GoodsGroup.objects.all()
    context = {
        'groups': groups,
        'menu': menu,
        'title': 'Про сайт',
    }
    return render(request, 'online_store/about.html', context=context)

def info(request):
    groups = GoodsGroup.objects.all()
    context = {
        'groups': groups,
        'menu': menu,
        'title': 'Інформація',
    }
    return render(request, 'online_store/info.html', context=context)

def add_basket(request):
    goods = Goods.objects.get(id=request.POST['goods_id'])
    b = Basket()
    b.user_id = request.POST['user_id']
    b.goods_id = request.POST['goods_id']
    b.amount = 1
    b.price = goods.price
    b.save()

    groups = GoodsGroup.objects.all()
    context = {
        'groups': groups,
        'menu': menu,
        'title': 'Кошик',
    }

    return render(request, 'online_store/home.html', context=context)


def basket(request):
    bas = Basket.objects.filter(user_id=request.user.id)
    groups = GoodsGroup.objects.all()

    context = {
        'bas': bas,
        'groups': groups,
        'menu': menu,
        'title': 'Кошик',
    }
    return render(request, 'online_store/basket.html', context=context)

# def get_total_price(self):
#     получаем общую стоимость
#     return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

  # if request.method == 'POST':
    #     form = OrderNewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('goods_show')
    # else:
    #     form = OrderNewForm()


def product_review(request):
    return render(request, 'online_store/product_review.html', {'title': 'Відгук про товар' })


def goods_new(request):
    if request.method == 'POST':
        form = GoodsNewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GoodsNewForm()

    context = {
        'form': form,
        'menu': menu,
        'title': 'Введення нового товару',
    }

    return render(request, 'online_store/goods_new.html', context=context)

# def archive(request: HttpRequest, year: int) -> HttpResponse:
#     if int(year) > 2021:
#         raise Http404()
#     return HttpResponse(f"<h1>Архів за роками</h1><p>{year}</p>")
#
#
# def archive_red(request: HttpRequest, year: int) -> HttpResponse:
#     if int(year) > 2021:
#         return redirect('home', permanent=True)
#         # обработка redirect 301-перемещение на постоянный url, 302-на временный
#     return HttpResponse(f"<h1>Архів за роками</h1><p>{year}</p>")

# def groups(request: HttpRequest) -> HttpResponse:
#     return HttpResponse(f"<h1>Групи товарів</h1>")

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm  # UserCreationForm - стандартная форма
    template_name = 'online_store/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm   #  AuthenticationForm - стандартная форма
    template_name = 'online_store/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
