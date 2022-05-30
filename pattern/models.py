from django.db import models


# Create your models here.
class ClassPattern(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(default=1)
    description = models.TextField()

    def __str__(self):
        return self.name


class SHACLPattern(models.Model):
    pattern_class = models.ForeignKey(ClassPattern, on_delete=models.CASCADE)
    order = models.IntegerField(default=1)
    code = models.CharField(max_length=10)
    shacl_pattern = models.TextField(default="")
    description = models.TextField()

    def __str__(self):
        return f"{self.pattern_class.name} - {self.code}"
