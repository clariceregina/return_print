# Conversor de Temperatura: Celsius para Fahrenheit

Este é um script em Python que converte uma temperatura fornecida em graus Celsius para Fahrenheit.

## Descrição

O código permite ao usuário inserir um valor de temperatura em Celsius, realiza a conversão para Fahrenheit e imprime o resultado. A fórmula utilizada para a conversão é a seguinte:

\[
Fahrenheit = (Celsius \times \frac{9}{5}) + 32
\]

## Como funciona

1. O script solicita ao usuário que insira um valor em Celsius.
2. Ele converte esse valor para Fahrenheit usando a fórmula mencionada.
3. O resultado da conversão é mostrado na tela.

## Exemplo de uso

```python
# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit():
    celsius_a = float(input('Insira o valor da temperatura em Celsius: '))
    fahrenheit = (celsius_a * (9/5)) + 32
    return fahrenheit

# Executa a função e exibe o resultado
resultado = celsius_para_fahrenheit()
print(f'A temperatura equivale a {resultado}°F')
