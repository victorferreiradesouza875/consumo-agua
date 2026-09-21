# 💧 Classificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Tipo](https://img.shields.io/badge/tipo-CLI-blue)
![Idioma](https://img.shields.io/badge/idioma-pt--BR-green)

Programa em Python que recebe o **tipo de imóvel** e o **consumo mensal de água (m³)** e exibe uma classificação de acordo com regras de negócio pré-definidas.

## Funcionalidades

- Solicita o tipo do imóvel (`comercial`, `apartamento` ou `casa`).
- Solicita o consumo mensal em metros cúbicos (número decimal).
- Aceita vírgula ou ponto como separador decimal (`12,5` ou `12.5`).
- Exibe a mensagem de classificação correspondente.

## Regras de negócio

As regras são avaliadas **de cima para baixo**, e a primeira condição verdadeira é a que vale.

| # | Condição | Mensagem exibida |
|---|----------|------------------|
| 1 | Tipo é `comercial` | Tarifa comercial aplicada – consulte o plano corporativo. |
| 2 | Tipo é `apartamento` **e** consumo < 10 m³ | Consumo econômico – excelente controle de água! |
| 3 | Tipo é `apartamento` **ou** `casa` **e** consumo ≤ 25 m³ | Consumo moderado – dentro do padrão residencial. |
| 4 | Qualquer outro caso | Consumo excessivo – adote medidas de economia e verifique vazamentos. |

## Requisitos

- Python 3.6 ou superior

## Como executar

1. Salve o código em um arquivo, por exemplo `consumo_agua.py`.
2. No terminal, execute:

```bash
python consumo_agua.py
```

## Exemplo de uso

```
Tipo (comercial/apartamento/casa): apartamento
Informe o consumo mensal de água em m³: 8,5
Consumo econômico – excelente controle de água!
```

## Casos de teste

| Tipo | Consumo (m³) | Resultado esperado |
|------|--------------|--------------------|
| comercial | 100 | Tarifa comercial aplicada |
| apartamento | 8 | Consumo econômico |
| apartamento | 15 | Consumo moderado |
| casa | 8 | Consumo moderado |
| casa | 25 | Consumo moderado |
| casa | 30 | Consumo excessivo |

## Código

```python
tipo = input("Tipo (comercial/apartamento/casa): ").lower()
consumo = float(input("Informe o consumo mensal de água em m³: ").replace(",", "."))

if tipo == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")
elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
```

## Como funciona

- `input()` lê os dados digitados pelo usuário.
- `.lower()` converte o tipo para minúsculas, evitando erro se o usuário digitar `Casa` ou `COMERCIAL`.
- `.replace(",", ".")` troca a vírgula por ponto para que o `float()` consiga converter o número.
- A estrutura `if / elif / else` aplica as regras na ordem, e os operadores `and` (e) e `or` (ou) combinam as condições.

## Limitações conhecidas

- Não há validação de entrada: se o usuário digitar um consumo que não seja número, o programa encerra com erro.
- Um tipo de imóvel diferente dos três previstos cai na regra 4 (consumo excessivo).

## Autor

Victor Ferreira de Souza 
