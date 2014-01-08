from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from goudimel.renderers.custom_html_renderer import CustomHTMLRenderer
from goudimel.helpers.solrsearch import SolrSearch

class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(APIView):
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)

    def get(self, request, *args, **kwargs):
        querydict = request.GET
        
        s = SolrSearch(request)
        facets = s.facets(['publisher', 'composer_src', 'forces'])

        if not querydict:
            result = {'results': [], 'facets': facets.facet_counts }
            return Response(result)

        search_results = s.search()
        result = {'results': search_results, 'facets': facets.facet_counts}

        return Response(result)
