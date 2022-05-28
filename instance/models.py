from django.db import models

from pattern.models import SHACLPattern


# Create your models here.
class PatternInstance(models.Model):
    shacl_pattern = models.ForeignKey(SHACLPattern, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    creator = models.CharField(max_length=100, default="anonymous")
    created_at = models.DateTimeField(auto_now_add=True)
    shacl_shapes = models.TextField(default="")

    def __str__(self):
        return self.name
