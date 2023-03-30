from django.db import models

# Create your models here.


class Query(models.Model):
    name = models.TextField(max_length=110, null=False, blank=False)
    phone = models.TextField(max_length=110, null=False, blank=False)
    email = models.TextField(max_length=110, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
