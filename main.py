from src.importadores.importador_csv import ImportadorCSV
from src.importadores.importador_json import ImportadorJSON
# (Aqui você implementaria o ImportadorJSON de forma similar ao CSV)
from src.processadores.processador_dados import analisar_vendas, comparar_produtos_entre_fontes
from src.utils.gerenciador_relatorio import GerenciadorDeRelatorio

def main():
    # Instanciando importadores concretos
    imp_csv = ImportadorCSV('data/entrada/vendas_2025_01.csv')
    
    # Executando a importação
    dados_csv = imp_csv.importar()
    
    # (Para praticar, crie o importador JSON e carregue os dados dele também)
    imp_json = ImportadorJSON('data/entrada/vendas_2025_02.json')
    dados_json = imp_json.importar()
    
    # Processando os dados com as funções que usam 'collections' e o decorador
    analise_csv = analisar_vendas(dados_csv)
    # analise_json = analisar_vendas(dados_json)

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

    # Comparando os produtos (descomente quando tiver o importador JSON)
    # comparar_produtos_entre_fontes(analise_csv, analise_json)


if __name__ == "__main__":
    main()