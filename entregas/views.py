
from django.http import HttpResponse


def lista_entregas(request):
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
            <tr>
                <td>1001</td>
                <td>Cliente Exemplo A</td>
                <td>Motorista A</td>
                <td>Pendente</td>
            </tr>
            <tr>
                <td>1002</td>
                <td>Cliente Exemplo B</td>
                <td>Motorista B</td>
                <td>Em andamento</td>
            </tr>
            <tr>
                <td>1003</td>
                <td>Cliente Exemplo C</td>
                <td>Motorista C</td>
                <td>Entregue</td>
            </tr>
        </table>
        <p>Dados demonstrativos para validação da interface.</p>
    </body>
    </html>
    """
    return HttpResponse(html)
