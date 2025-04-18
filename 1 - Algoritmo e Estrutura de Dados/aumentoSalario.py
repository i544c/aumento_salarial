def aumento():
    salario = float(input("Por favor, digite seu salário R$: "))

    # determinar a porcentagem do aumento
    if salario <= 2000:
        percentual = 0.2
        aument = salario * percentual
        novoSalario = salario + aument
        print(f" Seu aumento foi de R$ : {aument:.2f} \n e agora seu novo salário é R$ {novoSalario:.2f}")

    elif 2000 < salario <= 4000:
        percentual = 0.15
        aument = salario * percentual
        novoSalario = salario + aument
        print(f" Seu aumento foi de R$ : {aument:.2f} \n e agora seu novo salário é R$ {novoSalario:.2f}")

    elif 4000 < salario <= 8000:
        percentual = 0.10
        aument = salario * percentual
        novoSalario = salario + aument
        print(f" Seu aumento foi de R$ : {aument:.2f} \n e agora seu novo salário é R$ {novoSalario:.2f}")

    else:
        percentual = 0.5
        aument = salario * percentual
        novoSalario = salario + aument
        print(f" Seu aumento foi de R$ : {aument:.2f} \n e agora seu novo salário é R$ {novoSalario:.2f}")

    # Chamar função
aumento()