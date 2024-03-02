salario_f = int(input("Olá vendedor, por favor, me informe seu salário fixo: "))
valor_v = int(input("Agora informe os valores das vendas das lojas: "))

comis = valor_v * 0.03
salario_t = salario_f + comis

if valor_v > 20000:
    salario_t = salario_t + 600
    print(f"Parabéns! você atingiu a meta! seu salário total é de {salario_t:.2f}".format())
    quit()
else:
    print(f"Seu salário total é de: {salario_t:.2f} ".format())
    quit()    