import json

from .proxy_models import get_search_item_info

class GeoreferenceMiddleware:
    """This middleware injects a little bit of extra information into the
    Layer and Document objects that are returned to the search page. This info
    is used to determine which georeferencing-related links and text to place
    in the item's search results box."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        path = request.path
        api_paths = [
            '/api/documents/',
            '/api/layers/',
            '/api/maps/',
            '/api/base/',
        ]
        if path in api_paths:
            data = json.loads(response._container[0].decode("utf-8"))
            for item in data['objects']:

                try:
                    resource_type = item['detail_url'].split("/")[1].rstrip("s")
                    item['resource_type'] = resource_type
                except IndexError:
                    item['resource_type'] = ""
                    continue

                if resource_type in ['document', 'layer']:
                    info = get_search_item_info(resource_type, item['id'])

                    # set the output item properties
                    item['georeference_links'] = info['georeference_links']
                    item['georeferencing_status'] = info['georeference_status']
                else:
                    item['georeference_links'] = []
                    item['georeferencing_status'] = "n/a"

            response._container = [json.dumps(data).encode()]
        return response