import json
from collections import namedtuple
from .base import Importador
from src.utils.mixins import LogMixin

Venda = namedtuple('Venda', ['produto', 'preco', 'quantidade'])

class ImportadorJSON(Importador, LogMixin):
    
    def importar(self):
        self.log(f"Iniciando importação do arquivo JSON: {self.caminho_arquivo}")
        dados = []
        try:
            with open(self.caminho_arquivo, mode='r', encoding='utf-8') as f:
                dados_json = json.load(f)
                # não há cabeçalho em JSON, então não preciso de next(dados_json)
                for item_dicionario in dados_json:
                    venda = Venda(
                        produto=item_dicionario['produto'],
                        preco=float(item_dicionario['preco']),
                        quantidade=int(item_dicionario['quantidade'])
                    )
                    dados.append(venda)
            self.log("Importação JSON concluída com sucesso.")
            return dados
        except FileNotFoundError:
            self.log(f"Arquivo não encontrado: {self.caminho_arquivo}", tipo='ERRO')
            return []
        except Exception as e:
            self.log(f"Ocorreu um erro: {e}", tipo='ERRO')
            return []