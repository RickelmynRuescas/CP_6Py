# ✅ Checkpoint – Problema da Mochila 0/1  
FIAP – Estruturas de Dados  
Turma: 2ESA

---

## 👥 Integrantes

| Nome | RM |
|------|------|
| Rickelmyn de Souza Ruescas | 556055 |
| Fabrini Soares | 557813 |
| Vitor Couto Victorino | 554965 |

---

# 🎒 O Problema da Mochila 0/1

O Problema da Mochila (Knapsack Problem) é um clássico da Computação e consiste em selecionar itens com **peso** e **valor**, de forma que a soma dos pesos não ultrapasse a capacidade da mochila e o **valor total seja maximizado**.

### Premissas:

- Não é permitido levar frações de um item.
- Cada item pode ser tomado **0 ou 1 vez**.
- Pesos e valores são inteiros.

### Objetivo:

> **Maximizar o valor total transportado, sem ultrapassar a capacidade W da mochila.**

---

# 🧠 Natureza do Problema

O problema é classificado como um **Problema de Otimização Combinatória**.  
Para N itens, existem `2^N` possíveis subconjuntos — por isso a estratégia ingênua é exponencial.

---

# 📚 Programação Dinâmica (PD)

A Programação Dinâmica é uma técnica utilizada quando um problema apresenta:

### ✅ **Subestrutura ótima**  
A solução ótima do problema depende das soluções ótimas de subproblemas menores.

### ✅ **Subproblemas sobrepostos**  
Durante a solução, os mesmos subproblemas aparecem repetidas vezes.

É justamente isso que torna memoização e PD ferramentas essenciais.

---

# ✅ Abordagens Implementadas

Foram desenvolvidos **quatro algoritmos** para resolver o problema.

---

# 1️⃣ Estratégia Gulosa (Iterativa)

### ✔ Conceito  
Ordena os itens por **valor/peso** e pega os mais eficientes primeiro.

### ❌ Problema  
No caso da mochila 0/1, essa heurística **não garante a solução ótima**, pois não testa combinações.

### 📘 Complexidade  
- **O(n log n)** (por causa da ordenação)

### 🧪 Exemplo de falha  
Itens:  
- A = (2 kg, 10)
- C = (4 kg, 20)  
Valor/Peso = 5

- B = (3 kg, 12)  
Valor/Peso = 4

Guloso escolheria A e B → **Valor 22**  
Ótimo é A + C → **Valor 30**

---

# 2️⃣ Recursão Pura (Ingênua)

### ✔ Conceito  
Explora todas as combinações possíveis de incluir ou excluir cada item.

### ❌ Problema  
Repete subproblemas inúmeras vezes — extremamente lento.

### 📘 Complexidade  
- **O(2^n)**  
- Péssimo para entradas grandes

---

# 3️⃣ Recursão com Memoização (Top-Down)

### ✔ Conceito  
Versão otimizada da recursão pura utilizando um **cache** (dicionário).

### Vantagem  
Evita recomputação — cada subproblema é resolvido apenas **uma vez**.

### 📘 Complexidade  
- **O(nW)**

---

# 4️⃣ Programação Dinâmica (Bottom-Up)

### ✔ Conceito  
Constrói uma tabela `dp[i][w]` com as melhores soluções para capacidades menores.

### ✔ Vantagem  
Mais eficiente e sem recursão — considerada a implementação mais estável.

### 📘 Complexidade  
- **O(nW)** (igual à memoização)
- Geralmente mais rápida devido à ausência de chamadas recursivas

---

# ✅ Tabela Comparativa das Abordagens

| Método | Tipo | Garante Ótimo? | Complexidade |
|--------|------|----------------|--------------|
| Estratégia Gulosa | Heurística | ❌ Não | O(n log n) |
| Recursiva Pura | Força Bruta | ✅ Sim | O(2^n) |
| Memoização (Top-Down) | PD | ✅ Sim | O(nW) |
| PD (Bottom-Up) | PD | ✅ Sim | O(nW) |

---

# ✅ Conclusão

A Programação Dinâmica (Bottom-Up) é a **melhor abordagem**:

✅ Garante solução ótima  
✅ Funciona mesmo com muitos itens  
✅ Evita redundância  
✅ Melhor desempenho prático  

A recursiva pura é inviável para grandes entradas, e a gulosa funciona apenas como heurística — não como solução global.

---

# ✅ Execução

Para rodar o programa:

```bash
pip install prettytable
python app.py
