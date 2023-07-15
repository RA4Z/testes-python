def loop_inserir_texto():
    while True:
        try:
            texto = int(input('Insira um número válido: '))
            break
        except ValueError:
            print('Já avisei, você DEVE digitar um número!')

    print(f'Parabéns, você conseguiu!')

def divisao_por_zero(x,y):
    try:
        resultado = x / y
        print(f'A resposta é {resultado}')
    except ZeroDivisionError:
        print('Erro de divisão por zero!')


divisao_por_zero(1,1)
