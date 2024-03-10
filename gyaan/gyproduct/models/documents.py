from django.db import models

from django.utils import timezone

from _gybase.models.base import BaseActiveTimeStampModel

from gyproduct.models.base import Category

class DocumentType(BaseActiveTimeStampModel):
    '''
       Document type definition
    '''
    name = models.CharField(max_length=151)
    description = models.TextField(blank=True, null=True)
    

class PublisherCategoryDocuments(BaseActiveTimeStampModel):
    '''
        This model defines all the documents related for publisher approval under a category
    '''
    documents = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_documents', help_text="Category for which docs is required")
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)
    issued_by = models.CharField()
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.documents.name, self.category.name)
    


        