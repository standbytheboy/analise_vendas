# Projeto de Estudos: Python Avançado

Este repositório é um ambiente de estudos prático, criado com o objetivo de aplicar e solidificar conceitos avançados da linguagem Python. O projeto simula uma pequena ferramenta de análise de dados de vendas, servindo como um cenário real para a utilização de diversas funcionalidades poderosas da linguagem.

O código aqui presente é intencionalmente didático, priorizando a clareza e a demonstração dos conceitos em detrimento da otimização para produção.

---

## 🚀 Tópicos Abordados

Este projeto foi estruturado para explorar os seguintes tópicos:

### 1. Estruturas de Dados Avançadas
- **Módulo `collections`**:
  - `collections.Counter`: Para contar a frequência de produtos vendidos.
  - `collections.defaultdict`: Para agrupar e somar valores de vendas por produto.
  - `collections.namedtuple`: Para criar uma estrutura de dados leve e legível para as vendas.
- **Conjuntos (`Sets`)**:
  - Utilização de operações como união, interseção e diferença para comparar conjuntos de produtos de diferentes fontes de dados.

### 2. Programação Orientada a Objetos (POO) Avançada
- **Classes Abstratas (`abc`)**:
  - Criação de uma interface `Importador` que define um "contrato" para todas as classes que importam dados, garantindo polimorfismo.
- **Herança Múltipla e Mixins**:
  - Uso de uma classe `LogMixin` para adicionar funcionalidade de logging de forma modular e reutilizável aos importadores.
- **Decoradores (`Decorators`)**:
  - Implementação de um decorador `@medir_tempo` para analisar a performance de funções críticas sem alterar sua lógica interna.

### 3. Gerenciamento de Contexto e Manipulação de Arquivos
- **Protocolo de Gerenciamento de Contexto**:
  - Criação de uma classe `GerenciadorDeRelatorio` com os métodos `__enter__` e `__exit__` para garantir que os recursos (arquivos de relatório) sejam abertos e fechados de forma segura.
- **Manipulação Avançada de Arquivos (IO)**:
  - Leitura de diferentes formatos de arquivo (CSV, JSON), com atenção ao `encoding` correto para manipulação de texto.

---

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma para facilitar o estudo:

```
analisador_vendas/
├── data/              # Contém os arquivos de entrada e saída
├── src/               # Contém todo o código fonte da aplicação
│   ├── processadores/ # Lógica de análise de dados (collections, sets)
│   ├── importadores/  # Classes para importar dados (POO, ABC, IO)
│   └── utils/         # Módulos reutilizáveis (Decorators, Mixins, Context Managers)
└── main.py            # Ponto de entrada que orquestra a execução do projeto
```

- **`main.py`**: Orquestra a execução, mostrando como as diferentes partes do projeto se conectam.
- **`/src`**: O coração da aplicação, onde cada subtópico de estudo é implementado em um módulo específico.
- **`/data`**: Usado para simular a leitura e escrita de dados, separando o código da informação.

---

## 🛠️ Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/standbytheboy/analise_vendas.git)
    cd nome-do-repositorio
    ```

2.  **(Opcional mas recomendado) Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    # venv\Scripts\activate
    # No Linux/macOS:
    # source venv/bin/activate
    ```

3.  **Execute o script principal:**
    ```bash
    python main.py
    ```

4.  **Explore os resultados:**
    - Observe a saída no terminal, que mostrará os logs e o tempo de execução.
    - Verifique o arquivo `data/saida/relatorio.txt` que foi gerado.
    - Navegue pelos arquivos em `/src` para entender como cada conceito foi aplicado.

A ideia é modificar o código, adicionar novos recursos e experimentar!
