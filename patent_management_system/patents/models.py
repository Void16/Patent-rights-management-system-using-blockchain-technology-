""" from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Patent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    document_url = models.CharField(max_length=200)
    filing_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
 """
from django.db import models
from django.contrib.auth.models import User

class Patent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ImageField(upload_to='patent_documents/', blank=True, null=True, default='')  # Update this field
    filing_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title