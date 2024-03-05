from _gybase.api.data_utils import BaseDataUtils

from gyproduct.models.base import (
    Category, Department, Topic, Eligibility, ProductGroup, Product,
    ResourceContents
    )


CategoryDataUtils = BaseDataUtils(Category)
DepartmentDataUtils = BaseDataUtils(Department)
TopicDataUtils = BaseDataUtils(Topic)
EligibilityDataUtils = BaseDataUtils(Eligibility)
ProductGroupDataUtils = BaseDataUtils(ProductGroup)
ProductDataUtils = BaseDataUtils(Product)
ResourceContentDataUtils = BaseDataUtils(ResourceContents)