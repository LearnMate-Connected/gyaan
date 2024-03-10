from django.urls import path

from gyproduct.api.views import CategoryDocumentViewset


urlpatterns = [
    path('get_category_docs/', CategoryDocumentViewset.as_view({
        'get': 'get_category_docs'}), name='get_category_docs'),
    
]