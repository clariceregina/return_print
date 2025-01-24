def celsius_para_fahrenheit():
    celsius_a = float(input('Insira o valor da temperatura em Celsius: '))
    fahrenheit = (celsius_a * (9/5) ) + 32
    #quando usamos return, o valor é devolvido ao chamador (à função), permitindo, assim, que ela seja usada para armazenar o valor em uma variável e ser utilizada posteriormente
    return fahrenheit

resultado = celsius_para_fahrenheit()
print(f'A temperatura equivale a {resultado}°F')

celsius_para_fahrenheit()