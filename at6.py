tipo_g = input("Informe o combustível que você utiliza: A - Álcool, G - Gasolina ou D - Diesel: ").upper()
quant_c = int(input("Agora, digite a quantidade de litros vendidos: "))

if tipo_g == 'A':
    total = quant_c * 3.9
    print(f"O total a pagar é: {total:.2f}")
    quit()

elif tipo_g == 'G':
    total = quant_c * 4.9
    print(f"O total a pagar é: {total:.2f}")
    quit()

elif tipo_g == 'D':
    total = quant_c * 5.9
    print(f"O total a pagar é: {total:.2f}")
    quit()

else:
    print("Erro Fatal! ")
    quit()
