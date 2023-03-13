from django.db import models

# Create your models here.
class TodoList(models.Model):
    titulo = models.CharField(max_length=100, blank=True, default='')
    detalhamento = models.TextField()
    concluido = models.BooleanField(default=False)
