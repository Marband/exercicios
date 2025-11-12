import random

numero1 = random.randint(1, 10)
numero2 = random.randint(1, 10)
numero3 = random.randint(1, 10)


resposta = int(input(f"Quanto que é {numero1} x {numero2} + {numero3} ? "))

resultado = numero1 * numero2 + numero3

if resposta == resultado:
   print("Ebaaa vc acertou!!! :)")

else:
   print("oh vc errou :(")