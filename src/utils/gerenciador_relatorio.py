class GerenciadorDeRelatorio:
    """
    Classe que implementa o protocolo de gerenciamento de contexto
    para criar e finalizar um arquivo de relatório.
    """
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.arquivo = None

    def __enter__(self):
        print(f"--- Iniciando Relatório em '{self.caminho_arquivo}' ---")
        # Abre o arquivo em modo de escrita de texto, com encoding seguro
        self.arquivo = open(self.caminho_arquivo, 'w', encoding='utf-8')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.arquivo:
            self.arquivo.close()
        # Se exc_type não for None, um erro ocorreu.
        if exc_type:
            print(f"Ocorreu um erro: {exc_val}")
        
        print("--- Relatório Finalizado ---")
        # Retornar False (ou nada) propaga a exceção, se houver.
        # Retornar True suprime a exceção.