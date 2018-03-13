from django.db import models
from django.core.urlresolvers import reverse


class Enrolled(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    social_security_number=models.IntegerField(unique=True,null=False)
    join_date=models.DateTimeField(auto_now_add=True)
    terminated_date=models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('agreements:index')