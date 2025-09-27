# src/utils/mixins.py

class LogMixin:
    """
    Mixin para adicionar uma funcionalidade de logging simples.
    Não é feita para ser usada sozinha, mas sim "misturada" a outras classes.
    """
    def log(self, msg, tipo='INFO'):
        print(f'[{tipo}] - {msg}')