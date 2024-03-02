horas_t = int(input("Olá, funcionário! por favor, digite as sua htps(horas trabalhadas por semana): "))
salario_h = int(input("Por favor, informe seu salário por hora: "))

salario_t = horas_t * salario_h

if horas_t > 40:
    acres = salario_t * 0.5
    total = salario_t + acres
    print("Você foi bonificado! seu salário total é {}".format(total))
    quit()
    
print("Seu salário total é: {}".format(salario_t))
quit()