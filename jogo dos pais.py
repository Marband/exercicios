print("=======Jogo dos pais=======")

idade = int(input("Qual é a idade do seu pai?"))

if idade < 30 and idade > 14:
    print("Seu pai é muito novo!!")
elif idade > 29 and idade <   50:
    print("Seu pai é muito sabio!!")
elif idade < 14:
    print("Seu pai não existe")
elif idade > 50 and idade < 99:
    print("Seu pai é muito experiente!!")
else:
    print ("seu pai provavelmente ja morreu")

print("=======Fim do jogo dos pais=======")