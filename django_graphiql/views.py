from django.views.generic import TemplateView
from django.conf import settings


class GraphiQL(TemplateView):
    template_name = 'graphiql/index.html'

    def get_context_data(self, **kwargs):
        context = super(GraphiQL, self).get_context_data(**kwargs)
        context['default_query'] = getattr(settings, 'GRAPHIQL_DEFAULT_QUERY', None)
        return context
