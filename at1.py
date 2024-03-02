nota_1 = int(input("Olá caro usuário, peço para informar a nota da primeira fase do jogo:"))
nota_2 = int(input("Agora, te peço a nota da segunda fase: "))
media = (nota_1 + nota_2)/2

if media >= 8: 
    print("A experiência do usuário foi boa! :) ")
else:
    print("A experiência do usuário foi regular! :( ")   

quit() 