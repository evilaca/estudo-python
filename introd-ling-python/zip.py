lista01 = [1,2,3,4,5]
lista02 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista03 = ["R$2,00","R$5,00","R$50,00","Muito","R$50.000,00"]

for numero, nome, preco in zip(lista01, lista02, lista03):
    print(numero, nome, preco)
