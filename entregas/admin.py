
from django.contrib import admin
from .models import Entrega


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "cliente",
        "motorista",
        "status",
        "data_cadastro",
    )

    list_filter = ("status",)
    search_fields = ("numero", "cliente", "motorista")
