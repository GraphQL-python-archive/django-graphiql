from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class GraphiQL(TemplateView):
    template_name = 'graphiql/index.html'
