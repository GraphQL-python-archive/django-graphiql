from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.conf import settings


class GraphiQL(TemplateView):
    template_name = 'graphiql/index.html'
    graphql_url = None

    def get_context_data(self, **kwargs):
        context = super(GraphiQL, self).get_context_data(**kwargs)
        default_query = getattr(settings, 'GRAPHIQL_DEFAULT_QUERY', None)
        graphql_url = getattr(settings, 'GRAPHIQL_GRAPHQL_URL', '/graphql')
        graphql_viewname = getattr(settings, 'GRAPHIQL_GRAPHQL_VIEWNAME', None)
        if graphql_viewname:
            graphql_url = reverse(graphql_viewname)

        query = self.request.GET.get('query', default_query)

        context['query'] = query
        context['variables'] = self.request.GET.get('variables', '')
        context['response'] = ''
        context['graphql_url'] = self.graphql_url or graphql_url
        return context
