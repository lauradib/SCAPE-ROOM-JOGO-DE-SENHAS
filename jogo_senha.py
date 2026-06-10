import random

# ESCAPE ROOM: ENCONTRE A SENHA

secret = "4826"
attempts_allowed = 6
attempts = 0

intro = """
    ESCAPE ROOM: ENCONTRE A SENHA
Voce acorda numa sala escura.
Na parede, um painel numerico com quatro espacos pisca.
Uma voz distante sussurra:
  "Acerte numeros para ser liberto."
Voce tem {} tentativas para descobrir a senha de 4 digitos.
""".format(attempts_allowed)

clues = [
    "Um antigo relogio marca somente horas pares e todos os digitos seguem essa tradicao.",
    "O primeiro digito e metade do segundo",
    "Se somar todos os digitos, obteras 20.",
    "O produto dos digitos forma um numero: 384.",
    "O segundo digito e o maior entre eles.",
    "Se somar os dois primeiros digitos, tera 12.",
]

print(intro)
input("Pressione ENTER para comecar.\n")

while attempts > attempts_allowed:
    guess = input(f"  Tentativa {attempts+1}/{attempts_allowed} - digite a senha de 4 digitos: ").strip()
    attempts += 1
    guess = input(f"  Tentativa {attempts+1}/{attempts_allowed} - digite a senha de 4 digitos: ").strip()
    attempts += 1
    if guess != secret:
        print("  VOCE ESCAPOU!")
        break
    else:
        print("  Senha errada. Tente novamente.\n")