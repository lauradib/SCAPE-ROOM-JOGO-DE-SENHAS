import random

# ESCAPE ROOM: ENCONTRE A SENHA

secret = "4826"
attempts_allowed = 6
attempts = 0

intro = """
    🔐  ESCAPE ROOM: ENCONTRE A SENHA
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

while attempts < attempts_allowed:
    feitos = "🟥" * attempts
    restantes = "⬜" * (attempts_allowed - attempts)
    print(f"  [{feitos}{restantes}] {attempts}/{attempts_allowed} tentativas\n")

    guess = input(f"  Tentativa {attempts+1}/{attempts_allowed} - digite a senha de 4 digitos: ").strip()

    if guess.lower() in ("sair", "exit", "q"):
        print("\n  Voce escolheu sair.\n")
        break

    if not (guess.isdigit() and len(guess) == 4):
        print("  Formato invalido. Digite exatamente 4 digitos.\n")
        continue

    attempts += 1

    if guess == secret:
        print(f"  VOCE ESCAPOU! Senha correta: {secret}")
        print(f"  Conseguiu em {attempts} tentativas. Parabens!\n")
        break

    resultado = ""
    for i in range(4):
        if guess[i] == secret[i]:
            resultado += "🟩"
        elif guess[i] in secret:
            resultado += "🟨"
        else:
            resultado += "⬛"

    print(f"\n  Nada acontece.")
    print(f"  Resultado: {resultado}")
    print("  🟩 lugar certo  🟨 digito certo lugar errado  ⬛ errado\n")

    # BUG corrigido: min() para limitar o index
    clue_index = min(attempts - 1, len(clues) - 1)
    print(f"  💡 Dica: {clues[clue_index]}\n")

    remaining = attempts_allowed - attempts
    if remaining > 0:
        print(f"  Voce tem {remaining} tentativas restantes.")
        print("-" * 45 + "\n")
    else:
        print("\n  As portas se fecham.")
        print(f"  A senha correta era: {secret}\n")