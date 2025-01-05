numeros = int(input("Digite a quantidade de números: "))
numero = []

for i in range(numeros):
     while True:
        try:
            valor = int(input(f"Digite o número mágico {i + 1}: "))
            if valor >= 0:
                numero.append(valor)
                break
            else:
                print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

print(numero)

def calcular_magia():
    
    numero_soma = sum(numero)
    calculo = numero_soma * numeros

    print(f'Saída Esperada: {calculo}')

calcular_magia()



