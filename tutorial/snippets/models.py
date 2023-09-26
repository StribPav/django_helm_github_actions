from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    class Meta:
        ordering = ['created']