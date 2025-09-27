from src.importadores.importador_csv import ImportadorCSV
from src.importadores.importador_json import ImportadorJSON
from src.processadores.processador_dados import analisar_vendas, comparar_produtos_entre_fontes
from src.utils.gerenciador_relatorio import GerenciadorDeRelatorio

def main():
    # Instanciando importadores concretos
    imp_csv = ImportadorCSV('data/entrada/vendas_2025_01.csv')
    # Executando a importação
    dados_csv = imp_csv.importar()
    
    # O mesmo com os dados recebidos em JSON
    imp_json = ImportadorJSON('data/entrada/vendas_2025_01.json')
    dados_json = imp_json.importar()
    
    # Processando os dados com as funções que usam 'collections' e o decorador
    analise_csv = analisar_vendas(dados_csv)
    analise_json = analisar_vendas(dados_json)

    # Usando o gerenciador de contexto para criar o relatório
    with GerenciadorDeRelatorio('data/saida/relatorio.txt') as relatorio:
        relatorio.write("Análise de Vendas - Fonte CSV\n")
        relatorio.write("=============================\n\n")

        relatorio.write("Top 3 Produtos Mais Vendidos:\n")
        for produto, contagem in analise_csv['produtos_mais_comuns']:
            relatorio.write(f"- {produto}: {contagem} vezes\n")
        
        relatorio.write("\nResumo Financeiro por Produto:\n")
        for produto, totais in analise_csv['resumo_por_produto'].items():
            relatorio.write(f"- {produto}: R$ {totais['total_arrecadado']:.2f} arrecadado ({totais['quantidade_vendida']} unidades)\n")

        relatorio.write("\n\nAnálise de Vendas - Fonte JSON\n")
        relatorio.write("=============================\n\n")

        relatorio.write("Top 3 Produtos Mais Vendidos:\n")
        for produto, contagem in analise_json['produtos_mais_comuns']:
            relatorio.write(f"- {produto}: {contagem} vezes\n")
        
        relatorio.write("\nResumo Financeiro por Produto:\n")
        for produto, totais in analise_json['resumo_por_produto'].items():
            relatorio.write(f"- {produto}: R$ {totais['total_arrecadado']:.2f} arrecadado ({totais['quantidade_vendida']} unidades)\n")

    # Comparando os produtos
    # comparar_produtos_entre_fontes(analise_csv, analise_json)


if __name__ == "__main__":
    main()