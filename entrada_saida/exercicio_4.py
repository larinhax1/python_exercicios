# Solicitar ao usuário que insira as notas das três provas
nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))
nota3 = float(input("Insira a nota da terceira prova: "))

# Calcular a média aritmética das notas
media = (nota1 + nota2 + nota3) / 3

# Exibir o resultado da média
print("A média das notas é:", media)