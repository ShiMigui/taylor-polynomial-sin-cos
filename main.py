import math

def options(text='', expected=None, default=None):
    if expected is None:
        raise ValueError("expected deve ser passado!")
    if default is not None:
        text = f"{text}\nEscolha (padrão = {default}): "
    while True:
        opt = input(text)
        if opt == '':
            return default
        if opt in expected:
            return opt
        print("Opção inválida!")

# Escolha da função
fn = options(
    "Escolha a função desejada:\n\t(1) sen(x)\n\t(2) cos(x)",
    expected=['1', '2'],
    default='1'
)

# Escolha da unidade
md = options(
    "Escolha a medida:\n\t(1) radianos\n\t(2) graus",
    expected=['1', '2'],
    default='1'
)

# Entrada do valor x
while True:
    try:
        x = float(input("Digite o valor de x: "))
        break
    except ValueError:
        print("Valor inválido!")

# Converte graus para radianos, se necessário
if md == '2':
    x = math.radians(x)

# Normaliza x para o intervalo [-pi, pi]
x %= 2 * math.pi
if x > math.pi:
    x -= 2 * math.pi

# Número de termos no polinômio de Taylor
while True:
    try:
        n = int(input("Quantos termos deseja no polinômio de Taylor? "))
        if n > 0:
            break
        else:
            print("Informe um número inteiro positivo.")
    except ValueError:
        print("Valor inválido!")

# Determina o deslocamento para sen(x) ou cos(x)
shift = 1 if fn == '1' else 0

# Cálculo do polinômio de Taylor
res = 0.0
sinal = 1
fatorial = 1
x2 = x * x
potencia = x if shift == 1 else 1

for i in range(n):
    exp = 2 * i + shift
    if i > 0:
        potencia *= x2
        fatorial *= (exp - 1) * exp
    res += sinal * potencia / fatorial
    sinal *= -1

# Valor real usando math
real = math.sin(x) if fn == '1' else math.cos(x)

# Resultados
print(f"\nResultado pelo polinômio de Taylor: {res}")
print(f"Resultado real com math: {real}")
