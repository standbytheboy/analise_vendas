from collections import Counter, defaultdict
from src.utils.decoradores import medir_tempo

@medir_tempo
def analisar_vendas(lista_de_vendas):
    # Recebe uma lista de namedtuples 'Venda' e retorna análises.

    if not lista_de_vendas:
        return {}

    # 1. collections.Counter: para contar os produtos mais vendidos
    contador_produtos = Counter(v.produto for v in lista_de_vendas)
    
    # 2. collections.defaultdict: para agrupar vendas por produto
    vendas_por_produto = defaultdict(lambda: {'total_arrecadado': 0, 'quantidade_vendida': 0})
    for venda in lista_de_vendas:
        vendas_por_produto[venda.produto]['total_arrecadado'] += venda.preco * venda.quantidade
        vendas_por_produto[venda.produto]['quantidade_vendida'] += venda.quantidade

    # 3. Conjuntos (sets): para encontrar os produtos únicos vendidos
    produtos_unicos = {v.produto for v in lista_de_vendas}

    return {
        'produtos_mais_comuns': contador_produtos.most_common(3),
        'resumo_por_produto': vendas_por_produto,
        'produtos_unicos': produtos_unicos
    }

def comparar_produtos_entre_fontes(analise1, analise2):
    """Usa operações de conjunto para comparar produtos de duas análises."""
    produtos1 = analise1.get('produtos_unicos', set())
    produtos2 = analise2.get('produtos_unicos', set())
    
    print("\n--- Comparação de Produtos entre Fontes ---")
    print(f"Produtos em comum (interseção): {produtos1 & produtos2}")
    print(f"Produtos apenas na primeira fonte (diferença): {produtos1 - produtos2}")
    print(f"Todos os produtos distintos (união): {produtos1 | produtos2}")