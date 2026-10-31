
import unittest
from pathlib import Path


class TestConfiguracaoProjeto(unittest.TestCase):

    def test_arquivos_django_existem(self):
        raiz = Path(__file__).resolve().parent.parent

        arquivos = [
            "manage.py",
            "requirements.txt",
            "config/__init__.py",
            "config/settings.py",
            "config/urls.py",
            "config/wsgi.py",
            "config/asgi.py",
        ]

        for arquivo in arquivos:
            with self.subTest(arquivo=arquivo):
                self.assertTrue(
                    (raiz / arquivo).is_file(),
                    f"Arquivo ausente: {arquivo}"
                )

    def test_dependencia_django_declarada(self):
        raiz = Path(__file__).resolve().parent.parent

        conteudo = (
            raiz / "requirements.txt"
        ).read_text(encoding="utf-8")

        self.assertIn("Django", conteudo)


if __name__ == "__main__":
    unittest.main()
