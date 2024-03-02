q_atu = int(input("Informe a quantidade atual de estoque: "))
q_max = int(input("Informe a quantidade máxima de estoque: "))
q_min = int(input("Informe a quantidade mínima de estoque: "))

media = (q_max + q_min)/2

if q_atu >= media:
    print("Não efetuar a compra! ")
else:
    print("Efetuar a compra! ")    