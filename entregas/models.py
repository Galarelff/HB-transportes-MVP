
from django.db import models


class Entrega(models.Model):
    STATUS_CHOICES = [
        ("Pendente", "Pendente"),
        ("Em andamento", "Em andamento"),
        ("Entregue", "Entregue"),
    ]

    numero = models.CharField(max_length=20, unique=True)
    cliente = models.CharField(max_length=150)
    motorista = models.CharField(max_length=150)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pendente",
    )

    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_cadastro"]
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"

    def __str__(self):
        return f"Entrega {self.numero} - {self.cliente}"
    