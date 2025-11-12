nomes = ("")
print("=========  Bem Vindo ao Marcelobot  =========")
print("Oque você quer conversar")

Marcelobot = {
    "oi": "olá",
    "como vai": " Vou bem e você",
    "vou bem": "que bom",
    "hello": "hello!!!!!",
    "qual é o seu nome": f"meu nome é {nomes}"

    }

while True:
    pergunta = input("você:   ")
    if pergunta == "sair" :
        print("Obrigado pela Vou bem e vocêconversa !!!")
        break

    if pergunta in Marcelobot :
        print("Marrcelobot:" ,Marcelobot[pergunta] )

    else:
        print("opa não consigo responder isso ainda !!!")