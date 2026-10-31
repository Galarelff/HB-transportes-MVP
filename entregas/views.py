
from django.http import HttpResponse
from django.utils.html import escape

from .models import Entrega


def lista_entregas(request):
    entregas = Entrega.objects.all()

    linhas = ""

    for entrega in entregas:
        linhas += f"""
        <tr>
            <td>{escape(entrega.numero)}</td>
            <td>{escape(entrega.cliente)}</td>
            <td>{escape(entrega.motorista)}</td>
            <td>{escape(entrega.status)}</td>
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
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>HB Transportes - Controle de Entregas</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f5f9;
                margin: 0;
                padding: 30px;
            }
            h1 { color: #17365d; }
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
