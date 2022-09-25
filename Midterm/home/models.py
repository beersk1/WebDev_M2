from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name + ' ' + self.category

    class Meta:
        verbose_name_plural = "Task"