import csv
from collections import namedtuple
from .base import Importador
from src.utils.mixins import LogMixin

# Usando namedtuple para uma estrutura de dados mais legível
Venda = namedtuple('Venda', ['produto', 'preco', 'quantidade'])

class ImportadorCSV(Importador, LogMixin): # <- Herança Múltipla aqui!
    """Implementação concreta para importar arquivos CSV."""
    
    def importar(self):
        self.log(f"Iniciando importação do arquivo CSV: {self.caminho_arquivo}")
        dados = []
        try:
            # Gerenciamento de contexto para garantir que o arquivo seja fechado
            with open(self.caminho_arquivo, mode='r', encoding='utf-8') as f:
                leitor = csv.reader(f)
                next(leitor) # Pula o cabeçalho
                for linha in leitor:
                    venda = Venda(
                        produto=linha[0],
                        preco=float(linha[1]),
                        quantidade=int(linha[2])
                    )
                    dados.append(venda)
            self.log("Importação CSV concluída com sucesso.")
            return dados
        except FileNotFoundError:
            self.log(f"Arquivo não encontrado: {self.caminho_arquivo}", tipo='ERRO')
            return []
        except Exception as e:
            self.log(f"Ocorreu um erro: {e}", tipo='ERRO')
            return []