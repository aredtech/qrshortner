from django.db import models

from common.models import CommonModel
from accounts.models import CustomUser

# Create your models here.
class ShortUrls(CommonModel):

    url = models.URLField(max_length=510)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    shorten_url = models.CharField(max_length=10, blank=True, null=True)
    count = models.IntegerField(null=True, blank=True)
