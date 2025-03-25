# Algoritmo MaxMin Select

Este projeto implementa o algoritmo MaxMin Select, que encontra o maior e o menor elemento de um array de forma recursiva usando a estratégia de divisão e conquista.

## Descrição do Projeto

O algoritmo MaxMin Select é uma implementação que utiliza a estratégia de divisão e conquista para encontrar o maior e o menor elemento de um array. A lógica do algoritmo é a seguinte:

1. **Caso Base 1**: Se o array tiver apenas um elemento, ele é tanto o máximo quanto o mínimo.
2. **Caso Base 2**: Se o array tiver dois elementos, comparamos uma vez para determinar qual é o maior e qual é o menor.
3. **Caso Recursivo**: Para arrays maiores que 2 elementos:
   - Dividimos o array ao meio
   - Recursivamente encontramos o máximo e mínimo da metade esquerda
   - Recursivamente encontramos o máximo e mínimo da metade direita
   - Combinamos os resultados comparando os máximos e mínimos das duas metades

### Implementação

```python
def max_min_select(arr):
    if len(arr) == 1:
        return arr[0], arr[0]  # Caso base 1

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])  # Caso base 2

    mid = len(arr) // 2
    left_min, left_max = max_min_select(arr[:mid])  # Recursão na metade esquerda
    right_min, right_max = max_min_select(arr[mid:])  # Recursão na metade direita

    return min(left_min, right_min), max(left_max, right_max)  # Combinação dos resultados
```

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Navegue até o diretório do projeto:

```bash
cd MaxMin-Select-Python-
```

3. Crie um ambiente virtual:

```bash
python -m venv venv
```

4. Ative o ambiente virtual:

- No Windows:

```bash
.\venv\Scripts\activate
```

- No Linux/Mac:

```bash
source venv/bin/activate
```

5. Execute o arquivo main.py:

```bash
python main.py
```

O programa irá executar com um array de exemplo [3, 1, 7, 9, 2, 8, 4, 6] e mostrará o menor e o maior elemento.

## Relatório Técnico

### Análise da Complexidade Assintótica

#### Método de Contagem de Operações

Vamos analisar o número de comparações em cada etapa do algoritmo:

1. **Caso Base 1** (n = 1): 0 comparações
2. **Caso Base 2** (n = 2): 1 comparação
3. **Caso Recursivo** (n > 2):
   - Divisão do array: O(1)
   - Duas chamadas recursivas: 2T(n/2)
   - Combinação dos resultados: 2 comparações (min e max)

A recorrência que representa o número de comparações é:
T(n) = 2T(n/2) + 2

Para n elementos, o total de comparações é:

- Nível 0: 2 comparações
- Nível 1: 4 comparações
- Nível 2: 8 comparações
- ...
- Nível log₂n: n comparações

Total de comparações = 2 + 4 + 8 + ... + n = 2n - 2

Portanto, a complexidade temporal é O(n).

#### Análise pelo Teorema Mestre

Considerando a recorrência:
T(n) = 2T(n/2) + O(1)

1. **Identificação dos parâmetros**:

   - a = 2 (número de subproblemas)
   - b = 2 (tamanho de cada subproblema)
   - f(n) = O(1) (custo da combinação)

2. **Cálculo de log_b(a)**:

   - log₂(2) = 1
   - p = 1

3. **Caso do Teorema Mestre**:

   - f(n) = O(1) = O(n^0)
   - Como p = 1 e f(n) = O(n^0), temos que 0 < 1
   - Portanto, estamos no Caso 1 do Teorema Mestre

4. **Solução assintótica**:
   - T(n) = Θ(n^log_b(a)) = Θ(n^1) = Θ(n)

Conclusão: O algoritmo MaxMin Select tem complexidade temporal O(n), tanto pela análise de contagem de operações quanto pela aplicação do Teorema Mestre.
