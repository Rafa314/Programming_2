num_cont = int(input("Olá! Por Favor, Informe o número da sua conta: "))
saldo = int(input("Agora informe o valor do seu saldo: "))
debito = int(input("Agora informe o valor do seu débito: "))
credito = int(input("E por fim, digite o valor do seu crédito: "))

saldo_a = saldo - debito + credito

if saldo_a < 0:
    print(f"O seu saldo atual é de {saldo_a}, sua conta está negativa! ")
else: 
    print(f"O seu saldo atual é de {saldo_a}, sua conta está positiva! ")
