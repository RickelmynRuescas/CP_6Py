from prettytable import PrettyTable

# -----------------------------
# FUNÇÕES DO PROBLEMA DA MOCHILA
# -----------------------------

def knapsack(pesos, valores, W):
    """
    Estratégia Gulosa (Iterativa).
    Ordena itens por valor/peso e pega os mais "eficientes".
    NÃO garante solução ótima para mochila 0/1.
    """
    itens = list(zip(pesos, valores))
    itens.sort(key=lambda x: x[1] / x[0], reverse=True)

    cap = W
    total = 0

    for peso, valor in itens:
        if peso <= cap:
            total += valor
            cap -= peso

    return total


def knapsackRec(pesos, valores, W, i=0):
    """
    Solução recursiva pura (sem memoização).
    Explora todas as combinações possíveis.
    Complexidade: O(2^n)
    """
    if i == len(pesos) or W == 0:
        return 0

    if pesos[i] > W:
        return knapsackRec(pesos, valores, W, i + 1)

    pega = valores[i] + knapsackRec(pesos, valores, W - pesos[i], i + 1)
    nao_pega = knapsackRec(pesos, valores, W, i + 1)

    return max(pega, nao_pega)


def knapsackMemo(pesos, valores, W):
    """
    Solução recursiva com memoização (Top-Down).
    Complexidade: O(nW)
    """
    memo = {}

    def solve(i, cap):
        if i == len(pesos) or cap == 0:
            return 0

        if (i, cap) in memo:
            return memo[(i, cap)]

        if pesos[i] > cap:
            result = solve(i + 1, cap)
        else:
            pega = valores[i] + solve(i + 1, cap - pesos[i])
            nao_pega = solve(i + 1, cap)
            result = max(pega, nao_pega)

        memo[(i, cap)] = result
        return result

    return solve(0, W)


def knapsackPD(pesos, valores, W):
    """
    Programação Dinâmica (Bottom-Up).
    Tabela dp[i][w] = melhor valor usando i itens e capacidade w.
    Complexidade: O(nW)
    """
    n = len(pesos)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        peso = pesos[i - 1]
        valor = valores[i - 1]
        for w in range(1, W + 1):
            if peso > w:
                dp[i][w] = dp[i - 1][w]
            else:
                pega = valor + dp[i - 1][w - peso]
                nao_pega = dp[i - 1][w]
                dp[i][w] = max(pega, nao_pega)

    return dp[n][W]


# -----------------------------
# INTERFACE DO SISTEMA
# -----------------------------

def mostrar_tabela_itens(pesos, valores):
    tabela = PrettyTable()
    tabela.field_names = ["Item", "Peso", "Valor", "Valor/Peso"]

    for i in range(len(pesos)):
        tabela.add_row([
            chr(65 + i),
            f"{pesos[i]} kg",
            f"R${valores[i]}",
            f"{valores[i] / pesos[i]:.2f}"
        ])

    print("\n📦 ITENS DISPONÍVEIS:\n")
    print(tabela)


def mostrar_resultados(pesos, valores, W):
    print("\n🔧 EXECUTANDO ALGORITMOS...\n")

    guloso = knapsack(pesos, valores, W)
    recursivo = knapsackRec(pesos, valores, W)
    memo = knapsackMemo(pesos, valores, W)
    pd = knapsackPD(pesos, valores, W)

    tabela = PrettyTable()
    tabela.field_names = ["Algoritmo", "Descrição", "Valor Obtido"]

    tabela.add_row(["Guloso", "Heurística (valor/peso)", guloso])
    tabela.add_row(["Recursivo Puro", "Explora todas combinações", recursivo])
    tabela.add_row(["Memoização", "Top-Down com cache", memo])
    tabela.add_row(["Programação Dinâmica", "Bottom-Up (ótimo)", pd])

    print(tabela)

    print("\n✅ SOLUÇÃO ÓTIMA ESPERADA: 30 (Itens A + C)")
    print("✅ RESULTADO (PD):", pd)


def main():
    print("\n==============================")
    print("   PROBLEMA DA MOCHILA 0/1")
    print("==============================")

    pesos = [2, 3, 4, 1]
    valores = [10, 12, 20, 3]
    capacidade = 6

    mostrar_tabela_itens(pesos, valores)

    print(f"\n🎒 CAPACIDADE DA MOCHILA: {capacidade} kg\n")

    mostrar_resultados(pesos, valores, capacidade)

    print("\n✅ Execução finalizada com sucesso!\n")


if __name__ == "__main__":
    main()