'''Escreva um programa Python que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha. '''

id_h1 = int(input("Qual é a idade do primeiro homem? : "))
id_h2 = int(input("E qual é a idade do segundo homem? : "))
id_m1 = int(input("Qual é a idade da primeira mulher? : "))
id_m2 = int(input("E qual é a idade da segunda mulher? : "))

if id_h1 == id_h2 or id_m1 == id_m2:
    print("As idades não são diferentes! ")
    exit()

if id_h1 > id_h2: 
    print("O homem 1 é mais velho que o segundo")
    homem_mv = id_h1
    homem_mn = id_h2
else:
    homem_mv = id_h2  
    homem_mn = id_h1  
if id_m1 > id_m2:
    print("A mulher 1 é mais velha que a segunda")
    mulher_mv = id_m1
    mulher_mn = id_m2
else: 
    mulher_mv = id_m2
    mulher_mn = id_m1

soma = homem_mv + mulher_mn
produto = homem_mn * mulher_mv

print(f"A soma das idades do homem mais velho com a mulher mais nova: {soma}; produto das idades do homem mais novo com a mulher mais velha: {produto} ")



