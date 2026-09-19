from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('processing', 'Procesando'),
        ('completed', 'Completado'),
        ('failed', 'Fallido'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    progress = models.IntegerField(default=0) # Guarda el porcentaje de 0 a 100
    result_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Archivo {self.id} - {self.status}"