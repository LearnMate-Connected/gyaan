from gyproduct.api.data_utils import CategoryDocsDataUtils

from  gyproduct.constants import CATEGORY_CHOICES


class CatgeoryDocumentsUtils:
    cat_docs_data_class = CategoryDocsDataUtils
    
    def get_category_docs(self, user, **kwargs):
        f_dict = dict()
        category_name = kwargs.get("category_name")
        if category_name:
            if category_name not in CATEGORY_CHOICES:
                return {"error": "This category doesn't exist in our system"}, 400
            f_dict["category_name"] = category_name
        doc_type = kwargs.get("doc_type")
        if doc_type:
            f_dict["doc_type"] = doc_type
        is_required = kwargs.get("required")
        if is_required is not None:
            f_dict["is_required"] = is_required
        category_docs = list(self.cat_docs_data_class.filter(**f_dict).values())
        return {"data": category_docs}, 200
        
        