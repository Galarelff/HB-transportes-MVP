from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.html import escape
from django.middleware.csrf import get_token

from .models import Entrega


def lista_entregas(request):
    entregas = Entrega.objects.all()
    token_csrf = get_token(request)

    linhas = ""

    for entrega in entregas:
        numero = escape(entrega.numero)
        cliente = escape(entrega.cliente)
        motorista = escape(entrega.motorista)

        opcoes = ""

        for status in ["Pendente", "Em andamento", "Entregue"]:
            selecionado = "selected" if entrega.status == status else ""

            opcoes += (
                f'<option value="{status}" {selecionado}>'
                f'{status}</option>'
            )

        linhas += f"""
        <tr>
            <td>{numero}</td>
            <td>{cliente}</td>
            <td>{motorista}</td>
            <td>
                <form method="post"
                      action="/entrega/{numero}/atualizar-status/">

                    <input type="hidden"
                           name="csrfmiddlewaretoken"
                           value="{token_csrf}">

                    <select name="status">
                        {opcoes}
                    </select>

                    <button type="submit">Atualizar</button>
                </form>
            </td>
        </tr>
        """

    if not entregas.exists():
        linhas = """
        <tr>
            <td colspan="4">Nenhuma entrega cadastrada.</td>
        </tr>
        """

    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1">

        <title>HB Transportes - Controle de Entregas</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f5f9;
                margin: 0;
                padding: 30px;
            }

            h1 {
                color: #17365d;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                background: white;
            }

            th, td {
                padding: 15px;
                border: 1px solid #ddd;
                text-align: left;
            }

            th {
                background: #17365d;
                color: white;
            }

            select {
                padding: 8px;
                margin-right: 8px;
            }

            button {
                padding: 9px 14px;
                background: #17365d;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            button:hover {
                background: #28558a;
            }
        </style>
    </head>

    <body>
        <h1>HB Transportes</h1>

        <h2>Painel de Controle de Entregas</h2>

        <table>
            <tr>
                <th>Entrega</th>
                <th>Cliente</th>
                <th>Motorista</th>
                <th>Status</th>
            </tr>

            CONTEUDO_DAS_ENTREGAS
        </table>

        <p>Informações consultadas no banco de dados.</p>
    </body>
    </html>
    """

    html = html.replace("CONTEUDO_DAS_ENTREGAS", linhas)

    return HttpResponse(html)


@login_required
@require_POST
def atualizar_status(request, numero):
    entrega = get_object_or_404(Entrega, numero=numero)

    novo_status = request.POST.get("status")

    status_permitidos = [
        "Pendente",
        "Em andamento",
        "Entregue",
    ]

    if novo_status in status_permitidos:
        entrega.status = novo_status
        entrega.save(update_fields=["status"])

    return redirect("lista_entregas")