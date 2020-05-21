# coding=utf-8
from django.views.generic import DetailView
from django.views.generic import TemplateView
from search_views.filters import BaseFilter
from search_views.views import SearchListView

from app.forms import ServicoSearchForm
from app.mixins.CustomMixins import UserLoggedMixin, CustomContextMixin
from app.models import Servico


class ServicoFilter(BaseFilter):
    search_fields = {
        'query': ['titulo', 'descricao'],
        'estado': {'operator': '__icontains', 'fields': ['profissional__estado']},
        'cidade': {'operator': '__icontains', 'fields': ['profissional__cidade']},
        'preco_min': {'operator': '__gte', 'fields': ['valor_base']},
        'preco_max': {'operator': '__lte', 'fields': ['valor_base']},
    }


class IndexView(UserLoggedMixin, CustomContextMixin, SearchListView):
    model = Servico
    template_name = 'index.html'
    paginate_by = 5
    context_object_name = 'servicos'
    ordering = '?'

    form_class = ServicoSearchForm
    filter_class = ServicoFilter

    def get_params_search(self):
        return self.request.GET

    def get_context_data(self, **kwargs):
        kwargs['params'] = self.get_params_search()
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        params = self.get_params_search()
        servicos = self.model.objects.all()
        if 'categoria' in params:
            servicos = servicos.filter(profissional__categoria__id=params['categoria'])
        categories = [str(key).replace('_filter', '') for key in params if '_filter' in key]
        if len(categories) > 0:
            servicos = servicos.filter(profissional__categoria_id__in=categories)
        if 'ordering' in params:
            servicos = servicos.order_by(params['ordering'])
        return servicos


class AreaProfissional(CustomContextMixin, TemplateView):
    template_name = 'area_profissionals.html'


class ViewServicoDetail(CustomContextMixin, DetailView):
    model = Servico
    template_name = 'item_detail.html'
    context_object_name = 'servico'
