from abc import ABC, abstractmethod

class Importador(ABC):
    """
    Interface para importadores de dados. Define um "contrato" que
    todas as classes filhas DEVEM seguir.
    Não é possível instanciar um objeto 'Importador' diretamente.
    """
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    @abstractmethod
    def importar(self):
        """Método abstrato para ler e processar os dados do arquivo."""
        pass