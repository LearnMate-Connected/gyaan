from _gybase.api.data_utils import BaseDataUtils

from gyproduct.models.base import (
    Category, Department, Topic, Eligibility, ProductGroup, Product,
    ResourceContents
    )
from gyproduct.models.documents import PublisherCategoryDocuments

class CategoryDataUtils(BaseDataUtils):
    model_name = Category

class DepartmentDataUtils(BaseDataUtils):
    model_name = Department


class TopicDataUtils(BaseDataUtils):
    model_name = Topic


class EligibilityDataUtils(BaseDataUtils):
    model_name = Eligibility


class ProductGroupDataUtils(BaseDataUtils):
    model_name = ProductGroup


class ProductDataUtils(BaseDataUtils):
    model_name = Product


# Documents data utils
class CategoryDocsDataUtils(BaseDataUtils):
    model_name = PublisherCategoryDocuments


class ResourceContentDataUtils(BaseDataUtils):
    model_name = ResourceContents


