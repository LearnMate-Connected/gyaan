from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from gyproduct.api.utils import CatgeoryDocumentsUtils

class CategoryDocumentViewset:
    view_class = CatgeoryDocumentsUtils
    
    def get_category_docs(self, request):
        resp, status_code = self.view_class.get_category_docs(
            request.user, request.query_params.dict())
        return Response(resp, status=status_code)
    
